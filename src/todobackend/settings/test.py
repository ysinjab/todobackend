from base import *
import os

# Installed Apps
INSTALLED_APPS += ('django_nose', )
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
TEST_OUTPUT_DIR = os.environ.get('TEST_OUTPUT_DIR','.')
NOSE_ARGS = [
  '--verbosity=2',                  # verbose output
  '--nologcapture',                 # don't output log capture
  '--with-coverage',                # activate coverage report
  '--cover-package=todo',           # coverage reports will apply to these packages
 # '--with-spec',                    # spec style tests
 # '--spec-color',
  '--with-xunit',                   # enable xunit plugin
  '--xunit-file=%s/unittests.xml' % TEST_OUTPUT_DIR,
  '--cover-xml',                    # produce XML coverage info
  '--cover-xml-file=%s/coverage.xml' % TEST_OUTPUT_DIR,
]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ.get('MYSQL_DATABASE','todobackend'),
#         'USER': os.environ.get('MYSQL_USER','root'),
#         'PASSWORD': os.environ.get('MYSQL_PASSWORD','123'),
#         'HOST': os.environ.get('MYSQL_HOST','0.0.0.0'),
#         'PORT': os.environ.get('MYSQL_PORT','32769'),
#     }
# }
DATABASES = {

        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('D_NAME','todobackend'),
        'USER': os.environ.get('D_USER','root'),
        'PASSWORD': os.environ.get('D_PASSWORD','123'),
        'HOST': os.environ.get('D_HOST','0.0.0.0'),
        'PORT': os.environ.get('D_PORT','5432'),
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'todobackend',
    #     'USER': 'ysinjab',
    #     'PASSWORD': '123',
    #     'HOST': 'localhost'
    # }
}