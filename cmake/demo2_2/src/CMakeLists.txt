# 使用option可选配置，option需要借助configure_file的xxx.h.in提供宏
# cd build; cmake ../src -DUSE_MY_MATH=OFF; cmake --build .
# cd build; cmake ../src; cmake-gui . ; cmake --build .
cmake_minimum_required(VERSION 3.10)

project(demo)

# add_executable(hello main.c)
add_executable(${PROJECT_NAME} main.cc)

option(USE_MY_MATH "use demo providedmath implementation" ON)

if(USE_MY_MATH)
    add_subdirectory(math_func)
    list(APPEND EXTRA_LIBS math_func)   # 列表
    list(APPEND EXTRA_INCLUDES "${PROJECT_SOURCE_DIR}/math_func")

    set(VAR1 "hi")
    list(APPEND TEST_LIST "/tmp/abc" "/tmp/edf")
    message("--->>>>>> use my math")
else()
    message("--->>>>>> don't use my math")
endif()

message("--->>>>>>xyz: ${PROJECT_SOURCE_DIR}")  # 打印
message("--->>>>>>xyz: ${PROJECT_BINARY_DIR}")
message("--->>>>>>xyz: ${TEST_LIST}")
message("--->>>>>>xyz: ${VAR1}")

# target_link_libraries(demo PUBLIC math_func)
target_link_libraries(demo PUBLIC ${EXTRA_LIBS})

# 将build的二进制目录路径添加，可以解决demo_config.h.in生成的demo_config.h被main.cc找到
# 其中 ${PROJECT_SOURCE_DIR}/math_func （或${EXTRA_INCLUDES}） 与 前面add_subdirectory是重复的吧，这里不要也行
# target_include_directories(
#     demo PUBLIC
#     ${PROJECT_BINARY_DIR}
#     "${PROJECT_SOURCE_DIR}/math_func"
# )
target_include_directories(
    demo PUBLIC
    ${PROJECT_BINARY_DIR}
    ${EXTRA_INCLUDES}
)
configure_file(demo_config.h.in demo_config.h)