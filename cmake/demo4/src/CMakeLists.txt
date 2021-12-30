cmake_minimum_required(VERSION 3.0.0)
project(demo VERSION 0.1.0)

include(CTest)
enable_testing()

add_executable(demo demo.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)

# add_subdirectory(../lib)          # error,不知道这个文件夹编译的二进制文件放哪，需要手动指定
add_subdirectory(../lib lib_bin)    # 手动指定这个文件夹编译的二进制文件放哪个目录
target_link_libraries(demo a)

