from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB

db = SQLAlchemy()

class Submission(db.Model):
    __tablename__ = "vasp_onboarding_submissions"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # All structured answers (keyed by mapping reference id)
    answers = db.Column(JSONB, nullable=False, default=dict)

    # Files (keyed by mapping ref id → stored filename(s))
    files = db.Column(JSONB, nullable=False, default=dict)

    # Wizard state (which section user reached last)
    current_section_index = db.Column(db.Integer, nullable=False, default=0)

    # Simple completion flag
    is_submitted = db.Column(db.Boolean, nullable=False, default=False)
