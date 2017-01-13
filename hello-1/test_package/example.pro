TEMPLATE = app
TARGET = example

CONFIG += static conan_basic_setup
CONFIG -= qt
include(conanbuildinfo.pri)

SOURCES += example.cpp
