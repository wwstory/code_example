# 通过install()设置编译的二进制文件和头文件.h放入指定目录
# cd build; cmake ../src; cmake --build .; cmake --install . --prefix "../install"
# cmake --install . （这会试图复制到/usr/local/目录下，但权限没有）
cmake_minimum_required(VERSION 3.10)

project(demo)

# add_executable(hello main.c)
add_executable(${PROJECT_NAME} main.cc)

add_subdirectory(math_func)

target_link_libraries(demo PUBLIC math_func)

# # 暂未发现用处
# # add the binary tree to the search path for include files
# # so that we will find TutorialConfig.h
target_include_directories(
    demo PUBLIC
    "${PROJECT_BINARY_DIR}"
    "${PROJECT_SOURCE_DIR}/math_func"
)

install(TARGETS demo DESTINATION bin)                                   # 安装  将demo二进制文件放入bin目录