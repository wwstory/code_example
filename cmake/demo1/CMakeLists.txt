# cmake config配置文件
# cmake .; make
cmake_minimum_required(VERSION 3.10)

project(demo VERSION 1.0)

# add_executable(hello main.c)
add_executable(${PROJECT_NAME} main.cc)
add_library(Hello hello.cc hello.h)
target_link_libraries(${PROJECT_NAME} Hello)

configure_file(HelloConfig.h.in HelloConfig.h)  # 手动创建HelloConfig.h.in
# target_include_directories(Hello PUBLIC
#                            "${PROJECT_BINARY_DIR}"
# )

# # specify the C++ standard
# set(CMAKE_CXX_STANDARD 11)
# set(CMAKE_CXX_STANDARD_REQUIRED True)