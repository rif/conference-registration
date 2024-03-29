from fabric.api import sudo, prompt, run, local, cd
from fabric.decorators import runs_once, hosts, task
from fabric.colors import green

@task
def ci():
    'Commit localy using mercurial'
    comment = prompt('Commit comment: ', default='another commit from fabric')
    local('hg ci -m "%s"' % comment)
    push()

@runs_once
def push():
    print(green('pushing...'))
    local('hg push')

@task
@hosts('rif@loose.upt.ro')
def deploy():
    'triggers hg pul on the server'
    print(green('deploying...'))
    push()
    'Deploy the app to the target environment'
    with cd('conference_registration'):
        run('hg pul -uv')


@task
@hosts('rif@loose.upt.ro')
def reload():
    'fires an apache graceful reload'
    print(green('reloading...'))
    sudo('/etc/init.d/apache2 reload')
