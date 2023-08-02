from pathlib import Path

from decouple import config
from dj_database_url import parse as db_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS", default=[], cast=lambda x: x.split(",")
)

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # 3rdy party
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "tailwind",
    "django_browser_reload",
    "djstripe",
    "django_htmx",
    "django_components",
    "django_components.safer_staticfiles",
    # apps
    "core.apps.CoreConfig",
    "theme.apps.ThemeConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                        "django_components.template_loader.Loader",
                    ],
                )
            ],
            "builtins": [
                "django_components.templatetags.component_tags",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": config(
        "DATABASE_URL",
        default=f"sqlite:///{BASE_DIR}/db.sqlite3",
        cast=db_url,
    )
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "components",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TAILWIND_APP_NAME = "theme"

INTERNAL_IPS = [
    "127.0.0.1",
]

STRIPE_LIVE_PUBLIC_KEY = config("STRIPE_LIVE_PUBLIC_KEY")
STRIPE_LIVE_SECRET_KEY = config("STRIPE_LIVE_SECRET_KEY")
STRIPE_TEST_PUBLIC_KEY = config("STRIPE_TEST_PUBLIC_KEY")
STRIPE_TEST_SECRET_KEY = config("STRIPE_TEST_SECRET_KEY")
STRIPE_LIVE_MODE = config("STRIPE_LIVE_MODE", default=True, cast=bool)
DJSTRIPE_WEBHOOK_SECRET = config("DJSTRIPE_WEBHOOK_SECRET")
DJSTRIPE_USE_NATIVE_JSON_FIELD = True
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"

AUTH_USER_MODEL = "core.User"


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False

SITE_ID = 1
