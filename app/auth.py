from flask_security import RoleMixin, UserMixin
from core.db import db
from core.view import BaseAdminView

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(80), unique = True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)
    active = db.Column(db.Boolean(), nullable = False)
    roles = db.relationship('Role', secondary = roles_users, backref = 'users')

    def __str__(self):
        return self.first_name + " " + self.last_name + " <" + self.email + ">"


class UserView(BaseAdminView):
    required_role = 'superadmin'
    column_display_all_relations = True
    column_editable_list = ['email', 'first_name', 'last_name']
    column_searchable_list = ['roles.name', 'email', 'first_name', 'last_name']
    column_exclude_list = ['password']
    column_details_exclude_list = ['password']
    column_filters = ['email', 'first_name', 'last_name']
    #list_template = "admin/list.html"
    can_export = True
    can_view_details = True
    can_create = True
    can_edit = False
    can_delete = False
    edit_modal = False
    create_modal = False
    details_modal = False