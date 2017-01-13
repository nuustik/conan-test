from conans import ConanFile
import os

class PkgTestConan(ConanFile):
    requires = "hello/0.1@armin/testing" % (username, channel)
    generators = "qmake"

    def build(self):
        os.chdir(self.conanfile_directory)
        self.run('qmake')
        self.run("make")

    def test(self):
        self.run("%s%sexample" % (self.conanfile_directory, os.sep))
