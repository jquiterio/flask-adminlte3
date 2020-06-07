from flask import Flask, url_for, render_template
from flask_migrate import Migrate
from flask_security import Security
from flask_security import SQLAlchemyUserDatastore
from flask_security.utils import encrypt_password
from flask_admin import helpers as admin_helpers
from flask_admin import menu

from core.view import View, LinkView
from core.db import db

from app.base.models import Revision
from app.base.views import RevisionView

from app.auth import User, Role, UserView

from app.mainview import MainView



app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)
db.app = app
migrate = Migrate(app, db)

user_store = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_store)



view = View(app, skin='black', name='Dashboard', short_name="<b>F</b>LTE3", template_mode='bootstrap4', long_name="<b>Flask</b>AdminLTE3", index_view=MainView(url="/"), url="/")

view.set_category_icon(name="Security", icon_value="fa-shield-alt")
view.add_view(UserView(User, db.session, name="Users", category="Security", menu_icon_value='fa-user-secret'))


view.set_category_icon(name = 'Site', icon_value = 'fa-address-card')
view.add_link(LinkView(name = 'GitHub', category = 'Site', url = 'https://github.com/jquiterio/flask-adminlte3',
                      icon_value = 'fa-github', target = "_blank"))



@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template = view.base_template,
        admin_view = view.index_view,
        h = admin_helpers,
        get_url = url_for
    )



if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    Migrate(app, db)
    with app.app_context():
        super_admin_role = Role(name = 'superadmin')
        admin_role = Role(name = 'users')
        db.session.add(super_admin_role)
        db.session.add(admin_role)
        db.session.commit()

        test_user = user_store.create_user(
            first_name = 'John',
            last_name = 'Doe',
            email = 'admin@admin.com',
            password = encrypt_password('admin'),
            roles = [super_admin_role, admin_role]
        )
        db.session.add(test_user)
        db.session.commit()
    
    app.run()
