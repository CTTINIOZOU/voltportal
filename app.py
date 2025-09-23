import os
from uuid import uuid4
from flask import Flask, render_template, redirect, url_for, request, send_from_directory
from flask_wtf import FlaskForm
from wtforms import SubmitField
from werkzeug.utils import secure_filename

from models import db, Submission
from schema import SECTIONS, SECTION_SLUGS
from forms_runtime import wtfield_for

UPLOAD_DIR = os.environ.get("UPLOAD_DIR", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

def _normalize_db_uri(uri: str) -> str:
    if uri.startswith("postgres://"):
        uri = "postgresql://" + uri.split("://", 1)[1]
    if uri.startswith("postgresql://") and "+psycopg" not in uri:
        uri = "postgresql+psycopg://" + uri.split("://", 1)[1]
    return uri

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "voltportalfe-secret")
    raw_uri = os.environ.get("DATABASE_URL", "postgresql://user:pass@localhost:5432/voltportal")
    app.config["SQLALCHEMY_DATABASE_URI"] = _normalize_db_uri(raw_uri)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["MAX_CONTENT_LENGTH"] = 64 * 1024 * 1024
    db.init_app(app)

        # Create tables at startup (Flask 3 removed before_first_request)
    with app.app_context():
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
            s = Submission.query.get(int(sid))
            if s: return s
        s = Submission()
        db.session.add(s); db.session.commit()
        return s

    def section_index_from_slug(slug):
        return SECTION_SLUGS.index(slug) if slug in SECTION_SLUGS else 0

    @app.route("/")
    def start():
        sub = load_or_create_submission()
        return redirect(url_for("section", slug=SECTION_SLUGS[0], sid=sub.id))

    @app.route("/section/<slug>", methods=["GET","POST"])
    def section(slug):
        idx = section_index_from_slug(slug)
        section = SECTIONS[idx]
        FormClass = build_form_class(section)
        sub = load_or_create_submission()
        form = FormClass()

        if request.method == "POST":
            for f in section["fields"]:
                key = f["mapping_ref"]
                ftype = f["type"]

                if ftype in ("text","number","textarea","select","date"):
                    if wtfield_for(f) is not None:
                        sub.answers[key] = getattr(form, key.replace(".", "_")).data
                elif ftype == "file":
                    files_saved = []
                    uploaded = [request.files.get(key)]
                    for file in uploaded:
                        if file and file.filename:
                            from uuid import uuid4
                            fname = secure_filename(file.filename)
                            u = f"{uuid4().hex}_{fname}"
                            file.save(os.path.join(UPLOAD_DIR, u))
                            files_saved.append(u)
                    if files_saved:
                        sub.files[key] = files_saved[0]

            if "submit_back" in request.form:
                prev_idx = max(0, idx - 1); sub.current_section_index = prev_idx
                db.session.commit()
                return redirect(url_for("section", slug=SECTION_SLUGS[prev_idx], sid=sub.id))

            is_last = (idx == len(SECTIONS)-1)
            if is_last and "submit_finish" in request.form:
                sub.is_submitted = True; db.session.commit()
                return redirect(url_for("success", sid=sub.id))

            next_idx = min(len(SECTIONS)-1, idx+1)
            sub.current_section_index = next_idx; db.session.commit()
            return redirect(url_for("section", slug=SECTION_SLUGS[next_idx], sid=sub.id))

        last = (idx == len(SECTIONS)-1)
        return render_template("section.html", section=section, form=form, sid=sub.id, is_first=(idx==0), is_last=last)

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
