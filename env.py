import os

# Load environment variables from .env file
from dotenv import load_dotenv

load_dotenv()

# Set default values for environment variables
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codestar.settings")
os.environ.setdefault("SECRET_KEY", "django-insecure-&m%gu-ez==#b@$+_t99xi_wgv()$4vr7#$-og^=x4rdhx6lh6j")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("ALLOWED_HOSTS", "djang.herokuapp.com")
os.environ.setdefault("DATABASE_URL", "postgres://your_username:your_password@localhost:5432/your_database_name")
