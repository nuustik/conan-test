from conans import ConanFile, tools
import os

class PkgTestConan(ConanFile):
    requires = "hello/0.1@armin/testing"
    generators = "qmake"
    settings = "os", "compiler", "arch", "build_type"

    def build(self):
        self.run('qmake ../.. -tp vc')
        vcvars = tools.vcvars_command(self.settings)
        self.run("%s && msbuild example.vcxproj /p:configuration=debug" % vcvars)

    def test(self):
        # #self.conanfile_directory
        self.run(".%sdebug%sexample" % (os.sep, os.sep))
