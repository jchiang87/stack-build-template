import subprocess

# Modify the setup/setup.sh script to set up the requested Stack
# packages using the most recent tags.
setup_script = open('setup/setup.sh', 'a')
for package in "{{cookiecutter.stack_packages}}".split():
    command = 'source setup/setup.sh; eups list %s | tail -1' % package
    listing = subprocess.check_output(command, shell=True, 
                                      executable='/bin/bash').split()
    while listing[-1] == 'setup':
        listing.pop()
    tag = listing[-1]
    setup_script.write('setup %(package)s -t %(tag)s\n' % locals())
setup_script.write('''eups declare {{cookiecutter.repo_name}} -r . -c
setup {{cookiecutter.repo_name}}\n''')
setup_script.close()
