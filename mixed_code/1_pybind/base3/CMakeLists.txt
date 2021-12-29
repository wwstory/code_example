cmake_minimum_required(VERSION 3.4)
project(demo VERSION 0.1.0)

add_library(demo SHARED demo.cpp)

# include_directories(/usr/include/python3.8)
# include_directories(/usr/local/lib/python3.8/dist-packages/pybind11/include)

find_package(pybind11 REQUIRED)  # or `add_subdirectory(pybind11)`  # 只需要apt install python3-pybind11即可
target_link_libraries(demo PRIVATE pybind11::pybind11)  # https://pybind11.readthedocs.io/en/stable/compiling.html#advanced-interface-library-targets

set_target_properties(demo PROPERTIES PREFIX "")    # python import必须前面无'lib'前缀
