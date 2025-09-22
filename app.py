import os
from uuid import uuid4
from datetime import datetime

from flask import Flask, render_template, redirect, url_for, request, flash, send_from_directory
from flask_wtf import FlaskForm
from wtforms import SubmitField
from werkzeug.utils import secure_filename

from models import db, Submission
from schema import SECTIONS, SECTION_SLUGS
from forms_runtime import wtfield_for

UPLOAD_DIR = os.environ.get("UPLOAD_DIR", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "voltportalfe-secret")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL", "postgresql://user:pass@localhost:5432/voltportal"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["MAX_CONTENT_LENGTH"] = 64 * 1024 * 1024  # 64MB uploads
    db.init_app(app)

    @app.before_first_request
    def init_db():
        db.create_all()

    def build_form_class(section):
        class DynamicSectionForm(FlaskForm):
            submit_next = SubmitField("Next →")
            submit_back = SubmitField("← Back")
            submit_finish = SubmitField("Submit ✓")
        for f in section["fields"]:
            wt = wtfield_for(f)
            if wt is not None:
                setattr(DynamicSectionForm, f['mapping_ref'].replace(".", "_"), wt)
        return DynamicSectionForm

    def load_or_create_submission():
        sid = request.args.get("sid") or request.form.get("sid")
        if sid:
            try:
                sub = Submission.query.get(int(sid))
            except Exception:
                sub = None
            if sub:
                return sub
        sub = Submission()
        db.session.add(sub)
        db.session.commit()
        return sub

    def section_index_from_slug(slug):
        try:
            return SECTION_SLUGS.index(slug)
        except ValueError:
            return 0

    @app.route("/")
    def start():
        sub = load_or_create_submission()
        return redirect(url_for("section", slug=SECTION_SLUGS[0], sid=sub.id))

    @app.route("/section/<slug>", methods=["GET", "POST"])
    def section(slug):
        section_idx = section_index_from_slug(slug)
        section = SECTIONS[section_idx]
        FormClass = build_form_class(section)
        sub = load_or_create_submission()
        form = FormClass()

        # Pre-fill
        for f in section["fields"]:
            key = f["mapping_ref"]
            val = sub.answers.get(key)
            if wtfield_for(f) is not None and val is not None:
                getattr(form, key.replace(".", "_")).data = val

        if request.method == "POST":
            # Persist per field
            for f in section["fields"]:
                key = f["mapping_ref"]
                ftype = f["type"]

                if ftype in ("text", "number", "textarea", "select", "date"):
                    if wtfield_for(f) is not None:
                        sub.answers[key] = getattr(form, key.replace(".", "_")).data

                elif ftype == "multicheck":
                    selected = request.form.getlist(key)
                    sub.answers[key] = selected
                    opt_map = []
                    for opt in f["options"]:
                        if opt["value"] in selected:
                            opt_map.append(opt["option_mapping_ref"])
                    sub.answers[f"{key}.__option_mapping_refs"] = opt_map

                elif ftype == "list":
                    items = [i for i in request.form.getlist(key) if i and i.strip()]
                    sub.answers[key] = items

                elif ftype == "file":
                    files_saved = []
                    if f.get("multiple"):
                        uploaded = request.files.getlist(key)
                    else:
                        uploaded = [request.files.get(key)]
                    for file in uploaded:
                        if file and file.filename:
                            fname = secure_filename(file.filename)
                            unique_name = f"{uuid4().hex}_{fname}"
                            file.save(os.path.join(UPLOAD_DIR, unique_name))
                            files_saved.append(unique_name)
                    if files_saved:
                        sub.files[key] = files_saved if f.get("multiple") else files_saved[0]

                elif ftype == "table":
                    rows = []
                    rowcount = f.get("rows", 0)
                    for i in range(rowcount):
                        row = {}
                        for col in f["columns"]:
                            form_key = f"{key}__{i}__{col['key']}"
                            row[col["key"]] = request.form.get(form_key)
                        rows.append(row)
                    sub.answers[key] = rows

            # Navigation
            if "submit_back" in request.form:
                prev_idx = max(0, section_idx - 1)
                sub.current_section_index = prev_idx
                db.session.commit()
                return redirect(url_for("section", slug=SECTION_SLUGS[prev_idx], sid=sub.id))

            is_last = (section_idx == len(SECTIONS) - 1)
            if is_last and "submit_finish" in request.form:
                sub.is_submitted = True
                db.session.commit()
                return redirect(url_for("success", sid=sub.id))

            next_idx = min(len(SECTIONS) - 1, section_idx + 1)
            sub.current_section_index = next_idx
            db.session.commit()
            return redirect(url_for("section", slug=SECTION_SLUGS[next_idx], sid=sub.id))

        last = (section_idx == len(SECTIONS) - 1)
        return render_template("section.html",
                               section=section, form=form, sid=sub.id,
                               is_first=(section_idx == 0), is_last=last)

    @app.route("/uploads/<path:filename>")
    def uploaded_file(filename):
        return send_from_directory(UPLOAD_DIR, filename, as_attachment=False)

    @app.route("/success")
    def success():
        sid = request.args.get("sid")
        return render_template("success.html", sid=sid)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
