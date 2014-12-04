from fabric.api import *

def reset_feeds():
    """
    Work on production environment
    """
    local('./manage.py sqlclear feeds | ./manage.py dbshell')
    local('./manage.py syncdb')
    local('./manage.py loaddata data/feeds.json')
    local('./manage.py update_feeds')

def update_data():
	local('./manage.py update_feeds')
	local('./manage.py import_tweets')

