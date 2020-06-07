from core.view import BaseAdminView
from core.db import db

class RevisionView(BaseAdminView):
  required_role = 'users'

