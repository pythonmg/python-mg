import os
import site

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pymg.settings.prd")

site.addsitedir('/home/lucasmagnum/.virtualenvs/pymg/lib/python2.7/site-packages')

activate_this = os.path.expanduser("~/.virtualenvs/pymg/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
