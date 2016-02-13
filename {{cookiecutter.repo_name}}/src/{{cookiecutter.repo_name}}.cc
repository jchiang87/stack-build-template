#include "lsst/pex/exceptions.h"
#include "desc/{{cookiecutter.repo_name|lower}}/{{cookiecutter.repo_name}}.h"

namespace desc {
namespace {{cookiecutter.repo_name|lower}} {
   
   {{cookiecutter.repo_name}}::
   {{cookiecutter.repo_name}}(const std::string & message) 
      : _message(message) {
   }

   std::string {{cookiecutter.repo_name}}::run(bool raise_error) {
      if (raise_error) {
         throw lsst::pex::exceptions::RuntimeError("{{cookiecutter.repo_name}}::run: error raised");
      }
      return _message;
   }

} // namespace {{cookiecutter.repo_name|lower}}
} // namespace desc
