TEMPLATE = app
TARGET = app

CONFIG += conan_basic_setup
CONFIG -= qt
include(conanbuildinfo.pri)

SOURCES += main.cpp
