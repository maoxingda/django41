from django.apps import AppConfig


class App001Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app001'
    default_site = 'app001.admin.MyAdminSite'
    admin_order = 1
