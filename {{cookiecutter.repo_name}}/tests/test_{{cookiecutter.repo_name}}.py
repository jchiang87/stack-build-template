"""
Example unit tests for {{cookiecutter.repo_name}} package
"""
import unittest
import desc.{{cookiecutter.repo_name|lower}}

class {{cookiecutter.repo_name}}TestCase(unittest.TestCase):
    def setUp(self):
        self.message = 'Hello, world'
        
    def tearDown(self):
        pass

    def test_run(self):
        foo = desc.{{cookiecutter.repo_name|lower}}.{{cookiecutter.repo_name}}(self.message)
        self.assertEquals(foo.run(), self.message)

    def test_failure(self):
        self.assertRaises(TypeError, desc.{{cookiecutter.repo_name|lower}}.{{cookiecutter.repo_name}})
        foo = desc.{{cookiecutter.repo_name|lower}}.{{cookiecutter.repo_name}}(self.message)
        self.assertRaises(RuntimeError, foo.run, True)

if __name__ == '__main__':
    unittest.main()
