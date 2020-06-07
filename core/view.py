from flask_admin.contrib import sqla
from flask_security import current_user
from flask import url_for, redirect, request, abort
from flask_admin import menu, AdminIndexView
from flask_admin.base import AdminIndexView
from flask_admin.form import SecureForm


from flask_admin._compat import as_unicode
from flask_admin import Admin
import hashlib
import urllib


class LinkView(menu.MenuLink):

    def __init__(self, name, url = None, endpoint = None, category = None, class_name = "None", icon_type = "fa",
                 icon_value = None, target = None):
        super(LinkView, self).__init__(name, url, endpoint, category, class_name, icon_type, icon_value, target)


class AbstractModelView(sqla.ModelView):

    def __init__(self, model, session, name = None, category = None, endpoint = None, url = None, static_folder = None,
                 menu_class_name = None, menu_icon_type = "fa", menu_icon_value = None):
        super(AbstractModelView, self).__init__(model, session, name, category, endpoint, url, static_folder, menu_class_name,
                                          menu_icon_type, menu_icon_value)
    
    # def update_model(self, form, model):
    #   for field in form:
    #     if (field.type == "BooleanField") and (field.name not in request.form):
    #       field.data = False
    #   return super(AbstractModelView, self).update_model(form, model)


class BaseAdminView(AbstractModelView):
  required_role = 'users'
  can_export = True
  can_view_details = True
  can_create = True
  can_edit = True
  can_delete = True
  edit_modal = True
  create_modal = True
  details_modal = True
  column_exclude_list = ['reviewed_date', 'created_date', 'modified_date', 'edited_date', 'deleted_date']
  form_base_class = SecureForm

  def is_accessible(self):
    if not current_user.is_active or not current_user.is_authenticated:
      return False

    if current_user.has_role(self.required_role):
      return True

    return False

  def _handle_view(self, name, **kwargs):
    if not self.is_accessible():
      if current_user.is_authenticated:
        abort(403)
      else:
        return redirect(url_for('security.login', next = request.url))


class View(Admin):
  def __init__(self, app = None, name = None, url = None, subdomain = None, index_view = None,
                translations_path = None, endpoint = None, static_url_path = None, base_template = None,
                category_icon_classes = None, short_name = None, long_name = None, template_mode='bootstrap4', skin = 'black'):
    super(View, self).__init__(app, name, url, subdomain, index_view, translations_path, endpoint,
                                    static_url_path, base_template, template_mode, category_icon_classes)
    self.short_name = short_name or name
    self.long_name = long_name or name
    self.skin = skin
    self.url = url
    self.template_mode = template_mode

    # db.app = app
    # db.init_app(app)
    # self.add_view(View(User, db.session, name = "Users", menu_icon_value = 'fa-user-secret'))

  def gravatar_image_url(self, email, default_url, size = 96):
    return "https://www.gravatar.com/avatar/" \
            + hashlib.md5(email.lower().encode('utf-8')).hexdigest() \
            + "?" + urllib.parse.urlencode({'d': default_url, 's': str(size)})

  def set_category_icon(self, name, icon_value, icon_type = "fa"):
    cat_text = as_unicode(name)
    category = self._menu_categories.get(cat_text)

    if category is not None:
      category.icon_type = icon_type
      category.icon_value = icon_value