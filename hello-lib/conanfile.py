from conans import ConanFile

class HelloConan(ConanFile):
    name = "hello"
    version = "0.1"
    exports = "*"
    generators = "qmake"
    settings = "os", "compiler", "arch", "build_type"

    def build(self):
        self.run('qmake')
        self.run("make")

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.a", dst="lib")

    def package_info(self):
        self.cpp_info.libs = ["hello"]
