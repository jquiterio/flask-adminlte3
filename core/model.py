from datetime import datetime
from .db import db
from sqlalchemy_utils import ArrowType, ChoiceType, auto_delete_orphans



class BaseModel:
  id = db.Column(db.Integer, primary_key=True)
  # reviewed_date = db.Column(db.DateTime)
  # created_date = db.Column(db.DateTime, default=datetime.now())
  # modified_date = db.Column(db.DateTime, default=datetime.now())
  # edited_date = db.Column(db.DateTime)
  # deleted_date = db.Column(db.DateTime)
  # status = db.Column(ChoiceType(STATUS), default="inactive")
  # workflow_status = db.Column(ChoiceType(WORKFLOW_STATUS), default="open")

  # if status == 1: workflow_status = 5
  # if workflow_status < 5: status = 0


  # class Settings(db.Model):
  #   id = db.Column(db.Integer, primary_key=True)
  #   key = db.Column(db.String(50), nullable=False)
  #   value = db.Column(db.String(50), nullable=False)

  
