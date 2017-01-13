from conans import ConanFile

class HelloConan(ConanFile):
    name = "main"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    exports = "*"
    generators = "qmake" # Not required, but useful
    requires = "hello/0.1@armin/testing"

    def build(self):
        self.run('qmake')
        self.run("make")

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.lib", dst="lib")
        self.copy("*.a", dst="lib")

    def package_info(self):
        self.cpp_info.libs = ["main"]
