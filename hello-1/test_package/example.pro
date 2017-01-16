
TEMPLATE = app
TARGET = example

CONFIG += console
CONFIG += conan_basic_setup
CONFIG += debug
include($$OUT_PWD/conanbuildinfo.pri)

CONFIG -= qt

SOURCES += example.cpp
