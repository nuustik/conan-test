from conans import ConanFile
import os

class PkgTestConan(ConanFile):
    requires = "hello/0.1@armin/testing"
    generators = "qmake"

    def build(self):
        self.run('qmake ../..')
        self.run("make")

    def test(self):
        #self.conanfile_directory
        self.run(".%stest" % (os.sep))
