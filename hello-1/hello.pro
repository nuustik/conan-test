TEMPLATE = lib
TARGET = hello

CONFIG += static conan_basic_setup
CONFIG -= qt
include(conanbuildinfo.pri)

SOURCES += hello.cpp
HEADERS += hello.h
