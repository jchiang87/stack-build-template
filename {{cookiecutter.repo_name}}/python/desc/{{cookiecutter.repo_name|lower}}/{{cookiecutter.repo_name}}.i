// -*- c++ -*-

%define {{cookiecutter.repo_name}}_DOCSTRING
"Swig-exposed classes for the {{cookiecutter.repo_name}} package"
%enddef

%feature("autodoc", "1");
%module(package="{{cookiecutter.repo_name}}", docstring={{cookiecutter.repo_name}}_DOCSTRING) {{cookiecutter.repo_name}}

%include "lsst/p_lsstSwig.i"
%lsst_exceptions()

%{
#include "desc/{{cookiecutter.repo_name|lower}}/{{cookiecutter.repo_name}}.h"
%}
%include "desc/{{cookiecutter.repo_name|lower}}/{{cookiecutter.repo_name}}.h"
