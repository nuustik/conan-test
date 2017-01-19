TEMPLATE = app
TARGET = test

CONFIG += conan_basic_setup
include($$OUT_PWD/conanbuildinfo.pri)

SOURCES += test.cpp
