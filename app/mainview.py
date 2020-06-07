from core.view import BaseAdminView
from flask_admin import AdminIndexView, expose
from core.db import db

class MainView(AdminIndexView):
  @expose("/")
  def index_view(self):
    return self.render('admin/dashboard.html', name="Dashboard")
    
  # @expose("/settings")
  # def settings(self):
  #   name = "Settings"
  #   return self.render(
  #     'admin/settings.html',
  #     name=name
  #     )

