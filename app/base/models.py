from core import db
from sqlalchemy import desc, event, func, orm
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy_utils import ArrowType, ChoiceType, auto_delete_orphans
from datetime import datetime
from core.view import BaseAdminView
from core.db import db
from core.model import BaseModel

class Revision(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = name = db.Column(db.String(50), nullable=False)