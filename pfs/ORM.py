from django.conf import settings
import logging.config

from polifeelstat import settings
settings.configure()

from pfs.models import Country, Article
import os
SECRET_KEY = 'qkjdy@n0ymj94%+c9&#y@9+j_k&%nx)qznpamnh()f(-7qdm8j'
#
#
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'polifeelstat.settings')

import django
django.setup()

a = Country.objects.filter(country = "Argentina").select_related('article')

print(a)


