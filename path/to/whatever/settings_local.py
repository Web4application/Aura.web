DEBUG = True
TEMPLATE_DEBUG = DEBUG

# don't want emails while developing
ADMINS = ()
MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'mydbname'
DATABASE_USER = 'mydbuser'
DATABASE_PASSWORD = 'password'
DATABASE_HOST = 'localhost'
DATABASE_PORT = ''

SECRET_KEY = 'random-string-of-ascii'

#[more user/machine specific settings]
