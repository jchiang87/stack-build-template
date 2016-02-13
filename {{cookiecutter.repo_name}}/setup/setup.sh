inst_dir=$( cd $(dirname $BASH_SOURCE)/../..; pwd -P )
if [ ! -d "$inst_dir/ups_db" ]; then
   mkdir $inst_dir/ups_db
fi
export LSSTSW={{cookiecutter.lsstsw_install_directory}}
export EUPS_PATH=$inst_dir:${LSSTSW}/stack
. ${LSSTSW}/bin/setup.sh
