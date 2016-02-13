#ifndef desc_{{cookiecutter.repo_name|lower}}_h
#define desc_{{cookiecutter.repo_name|lower}}_h

#include <string>

namespace desc {
namespace {{cookiecutter.repo_name|lower}} {

   class {{cookiecutter.repo_name}} {

   public:

      {{cookiecutter.repo_name}}(const std::string & message);

      std::string run(bool raise_error=false);

   private:
      
      std::string _message;

   };

} // namespace {{cookiecutter.repo_name|lower}} 
} // namespace desc

#endif // desc_{{cookiecutter.repo_name|lower}}_h
