# 子目录编译
# cd build; cmake ../src; cmake --build .
cmake_minimum_required(VERSION 3.10)

project(demo)

# add_executable(hello main.c)
add_executable(${PROJECT_NAME} main.cc)

add_subdirectory(math_func)

target_link_libraries(demo PUBLIC math_func)

# # 此处可不用
# # add the binary tree to the search path for include files
# # so that we will find TutorialConfig.h
# target_include_directories(
#     demo PUBLIC
#     "${PROJECT_BINARY_DIR}"
#     "${PROJECT_SOURCE_DIR}/math_func"
# )