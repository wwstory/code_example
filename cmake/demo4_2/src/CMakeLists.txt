cmake_minimum_required(VERSION 3.0.0)
project(demo VERSION 0.1.0)

include(CTest)
enable_testing()

add_executable(demo demo.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)

add_subdirectory(../lib lib_bin)
target_link_libraries(demo a)

include_directories(../include)     # 因为从这个开始编译，它没有include的环境变量

