from fabric.api import env, run, cd, sudo
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
        run("%s manage.py %s --settings=pymg.settings.production" % (
            PYTHON_BIN, args))


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
    manage('sqlclear feeds')
    manage('dbshell')
    manage('syncdb')
    manage('loaddata data/feeds.json')
    manage('update_feeds')


def update_data():
    manage('update_feeds')
