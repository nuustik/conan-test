from conans import ConanFile, tools

class HelloConan(ConanFile):
    name = "hello"
    version = "0.1"
    exports = "*"
    generators = "qmake"
    settings = "os", "compiler", "arch", "build_type"

    def build(self):
        self.run('qmake -tp vc')
        vcvars = tools.vcvars_command(self.settings)
        self.run("%s && msbuild hello.vcxproj /p:configuration=debug" % vcvars)

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]
