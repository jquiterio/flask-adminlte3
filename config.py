# Enable debug mode
DEVELOPMENT = True
DEBUG = True

# Create dummy secrey key so we can use sessions
SECRET_KEY = 'sVc7EesNgGsBXv3JW2NzQ5LJYnzqqkTs'

# Create in-memory database
DATABASE_FILE = 'flask-adminlte3.sqlite'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-Security config
SECURITY_URL_PREFIX = "/"
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = 'ghnpvhF5y8MsEBrNAavLXqeFJGU2RGhT'

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_REGISTER_URL = "/register/"
SECURITY_RESET_URL = "/reset/"

SECURITY_POST_LOGIN_VIEW = "/"
SECURITY_POST_LOGOUT_VIEW = "/"
SECURITY_POST_REGISTER_VIEW = "/"
SECURITY_POST_RESET_VIEW = "/"

# Flask-Security features
SECURITY_REGISTERABLE = False
SECURITY_RECOVERABLE = False
SECURITY_CHANGEABLE = False
SECURITY_SEND_REGISTER_EMAIL = False
