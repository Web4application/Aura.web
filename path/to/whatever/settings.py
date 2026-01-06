from ConfigParser import RawConfigParser

config = RawConfigParser()
config.read('/etc/whatever/settings.ini')

DATABASE_USER = config.get('database', 'DATABASE_USER')
DATABASE_PASSWORD = config.get('database', 'DATABASE_PASSWORD')
DATABASE_HOST = config.get('database', 'DATABASE_HOST')
DATABASE_PORT = config.get('database', 'DATABASE_PORT')
DATABASE_ENGINE = config.get('database', 'DATABASE_ENGINE')
DATABASE_NAME = config.get('database', 'DATABASE_NAME')
TEST_DATABASE_NAME = config.get('database', 'TESTSUITE_DATABASE_NAME')

SECRET_KEY = config.get('secrets','SECRET_KEY')
CSRF_MIDDLEWARE_SECRET = config.get('secrets', 'CSRF_MIDDLEWARE_SECRET')

SESSION_COOKIE_DOMAIN = config.get('cookies','SESSION_COOKIE_DOMAIN')

DEBUG = config.getboolean('debug','DEBUG')
TEMPLATE_DEBUG = config.getboolean('debug','TEMPLATE_DEBUG')
VIEW_TEST = config.getboolean('debug', 'VIEW_TEST')
INTERNAL_IPS = tuple(config.get('debug', 'INTERNAL_IPS').split())
if config.getboolean('debug', 'SKIP_CSRF_MIDDLEWARE'):
    MIDDLEWARE_CLASSES = tuple([x for x in list(MIDDLEWARE_CLASSES)
                                  if not x.endswith('CsrfMiddleware')])

SERVER_EMAIL = config.get('email', 'SERVER_EMAIL')
EMAIL_HOST = config.get('email', 'EMAIL_HOST')
ADMINS = tuple(config.items('error mail'))
MANAGERS = tuple(config.items('404 mail'))
