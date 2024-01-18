import os

os.environ.setdefault("DATABASE_URL", "postgres://ygkwkcqh:***@snuffleupagus.db.elephantsql.com/ygkwkcqh")


# Set the DEBUG mode (True for development, False for production)
DEBUG = True

# Add any other Django settings or custom environment variables you need
# For example:
# DATABASE_URL = 'your-database-url'

# Make sure to add the following lines to the end of your env.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codestar.settings')
