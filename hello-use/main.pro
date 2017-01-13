TEMPLATE = app
TARGET = main

CONFIG += static conan_basic_setup
CONFIG -= qt
include(conanbuildinfo.pri)

SOURCES += main.cpp
