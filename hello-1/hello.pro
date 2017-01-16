TEMPLATE = lib
TARGET = hello

CONFIG += static conan_basic_setup
CONFIG += debug
CONFIG -= qt
include(conanbuildinfo.pri)

SOURCES += hello.cpp
HEADERS += hello.h
