cmake_minimum_required(VERSION 3.0.0)
project(a VERSION 0.1.0)

add_library(a SHARED a.cpp)
include_directories(../include)
