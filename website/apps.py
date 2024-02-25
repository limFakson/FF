from django.apps import AppConfig
from dotenv import load_dotenv


class WebsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'website'

# Load environment variables from .env file
load_dotenv()