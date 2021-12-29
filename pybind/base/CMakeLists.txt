cmake_minimum_required(VERSION 3.0.0)
project(demo VERSION 0.1.0)

# 自动生成
# include(CTest)
# enable_testing()

# add_library(demo demo.cpp)
add_library(demo SHARED demo.cpp)

# 自动生成
# set(CPACK_PROJECT_NAME ${PROJECT_NAME})
# set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
# include(CPack)

# 先安装:
#   apt install python3-dev
#   pip3 install pybind11
# 需要包含 python3 -m pybind11 --includes 命令出现的include
include_directories(/usr/include/python3.8)
include_directories(/home/dejiang/venv/torch_env/lib/python3.8/site-packages/pybind11/include)
set_target_properties(demo PROPERTIES PREFIX "")    # python import必须前面无'lib'前缀

# 添加后缀(可选)
execute_process(
    COMMAND python3-config --extension-suffix
    OUTPUT_VARIABLE out_suffix
)
set_target_properties(demo PROPERTIES SUFFIX ${out_suffix})
message(STATUS "suffix output:\n${out_suffix}") # 打印消息
