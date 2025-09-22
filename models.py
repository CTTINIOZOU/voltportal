from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB

db = SQLAlchemy()

class Submission(db.Model):
    __tablename__ = "vasp_onboarding_submissions"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    answers = db.Column(JSONB, nullable=False, default=dict)
    files = db.Column(JSONB, nullable=False, default=dict)
    current_section_index = db.Column(db.Integer, nullable=False, default=0)
    is_submitted = db.Column(db.Boolean, nullable=False, default=False)
