cmake_minimum_required(VERSION 3.4)
project(demo VERSION 0.1.0)

# add_executable(demo demo.cpp)
add_library(demo SHARED demo.cpp)
set_target_properties(demo PROPERTIES PREFIX "")    # python import必须前面无'lib'前缀

find_package(pybind11 REQUIRED)
target_link_libraries(demo PRIVATE pybind11::embed)

