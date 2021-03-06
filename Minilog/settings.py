# vim: set fileencoding=utf-8 :

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# ファイルパスの指定は絶対パスで行うことが多いのでルートパスを
# 絶対パスとして取得しておく。なお __file__ は Python において
# コードが実行されているファイルの相対パスを指すのでこの位置を
# 基準にルートを決定する
import os
ROOT = os.path.dirname(__file__)
ROOT = os.path.join(ROOT, '../')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',         # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(ROOT, 'database.db'),      # Or path to database file if using sqlite3.
        'USER': '',                                     # Not used with sqlite3.
        'PASSWORD': '',                                 # Not used with sqlite3.
        'HOST': '',                                     # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                                     # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

    # プロジェクトとしての静的ファイル（画像・スクリプト・スタイルシートなど）を
    # 置く場所を追加する。なお各アプリ用の静的ファイルは各アプリ内の static
    # フォルダに置けば良い
    # Ref: https://docs.djangoproject.com/en/dev/howto/static-files/
    os.path.join(ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',

    # django-compressor で使用する
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'b$9(88_ts@d&amp;791l(rt78o0ttnwm+i!zcc3#s0lxuluovfr0d1'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # django-pagination で使用する
    'pagination.middleware.PaginationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    # この request はデフォルトでは含まれないが django-pagination
    # で使用するため追加する
    "django.core.context_processors.request",
)


ROOT_URLCONF = 'Minilog.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'Minilog.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT, 'template'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # DjangoのAdminサイトを使用するために追加
    'django.contrib.admin',
    # Django Templateにて |markdown フィルタを利用するために追加
    'django.contrib.markup',
    # Djangoにて簡単にページネーションをするためのライブラリ
    # （デフォルトの機能にもページネーションはあるが、こちらのほうが楽）
    'pagination',
    # JavaScript, CSS の minify, CoffeeScript, Lessのコンパイルなどを自動化
    # するためのプラグイン
    'compressor',
    # 自作のアプリ
    'blogs',
)

# django-compressor で CoffeeScript, Less, Sass, Scss を自動的にコンパイルする
# ための設定。それぞれの実行ファイルが環境に存在している必要がある
#
#   npm -g install coffeescript
#   npg -g install less
#
# などでインストールを予めおこなっておく
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
)
# django-compressor で CSS の minify に CSSMin を使用
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
# 強制的に django-compressor をONにする
# 通常はデプロイモード（DEBUG=False)の時のみONになる
COMPRESS_ENABLED = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
