from fabric.api import local, env, run, cd, sudo
from decouple import config


env.hosts = [
    config('DEPLOY_SERVER'),
]
env.password = config('DEPLOY_PASS')


PROJECT_PATH = u'/home/deploy/www/pugmg/project'
PYTHON_BIN = u'/home/deploy/.envs/pugmg/bin/python'
PIP_BIN = u'/home/deploy/.envs/pugmg/bin/pip'


def git(cmd):
    with cd(PROJECT_PATH):
        run("git %s" % cmd)


def pull():
    git("pull --rebase origin master")


def manage(args):
    with cd(PROJECT_PATH):
        run("%s manage.py %s" % (PYTHON_BIN, args))


def install_requirements():
    with cd(PROJECT_PATH):
        run("%s install -r requirements.txt" % PIP_BIN)


def reload_service():
    sudo("supervisorctl reload pugmg")


def deploy():
    pull()
    install_requirements()
    manage('syncdb --noinput')
    manage('collectstatic --noinput')
    reload_service()



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
