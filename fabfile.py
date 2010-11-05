from fabric.api import hosts, prompt, sudo, run, local, cd

def ci():
    """Commit localy using mercurial"""
    comment = prompt('Commit comment: ', default='another commit from fabric')
    local('hg ci -m "%s"' % comment)
    local('hg push')

"""
For running sudo on remote machine:
    vi /etc/sudoers (EDIT: please use visudo instead)
    comment out: #Default requiretty
"""
@hosts('horia@loose.upt.ro:22022')
def deploy():
    'Deploy the app to the target environment'
    local('hg push ssh://loose/../icsmreg/icsm_registration')
    with cd('/home/icsmreg/icsm_registration'):
        run('hg up')

@hosts('horia@loose.upt.ro:22022')
def reload():
    'fires an apache graceful reload'
    sudo('apache2ctl graceful')
