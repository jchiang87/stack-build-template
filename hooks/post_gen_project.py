import subprocess

# Modify the setup/setup.sh script to setup the requested Stack
# packages using the most recent tags.
setup_script = open('setup/setup.sh', 'a')
for package in "{{cookiecutter.stack_packages}}".split():
    command = 'source setup/setup.sh; eups list | grep %s | tail -1' % package
    tag = subprocess.check_output(command, shell=True, 
                                  executable='/bin/bash').split()[-1]
    setup_script.write('setup %(package)s -t %(tag)s\n' % locals())
setup_script.write('''eups declare {{cookiecutter.repo_name}} -r . -c
setup {{cookiecutter.repo_name}}\n''')
setup_script.close()
