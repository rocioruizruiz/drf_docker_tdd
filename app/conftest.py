import os
import pytest
from django.conf import settings


DEFAULT_ENGINE = "django.db.backends.postgresql_psycopg2"


# @pytest.fixture(scope="session")
# def django_db_setup():
#     settings.DATABASES["default"] = {
#         "ENGINE": os.environ.get("DB_TEST_ENGINE", DEFAULT_ENGINE),
#         "HOST": os.environ["DB_TEST_HOST"],
#         "PORT": os.environ["DB_TEST_PORT"],
#         "USER": os.environ["DB_TEST_USER"],
#         "PASSWORD": os.environ["DB_TEST_PASSWORD"],
#     }

@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }


@pytest.fixture(scope="module")
def foo():
    # set up code
    yield "bar"
    # tear down code


# all code before the yield statement serves as setup code
# while everything after serves as the teardown.
