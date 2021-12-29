# 测试
# cd build; cmake ../src; cmake --build .
cmake_minimum_required(VERSION 3.10)

project(demo)

# add_executable(hello main.c)
add_executable(${PROJECT_NAME} main.cc)

add_subdirectory(math_func)

target_link_libraries(demo PUBLIC math_func)



enable_testing()
add_test(NAME test1 COMMAND demo 2 4)                                                         # 单条测试

# # define a function to simplify adding tests
function(do_test1 target arg1 arg2 result)                                                    # 循环调用指定的测试函数
  add_test(NAME test_arg_${arg1}_${arg2} COMMAND ${target} ${arg1} ${arg2})                   # 设置测试名,设置测试的命令
  set_tests_properties(test_arg_${arg1}_${arg2} PROPERTIES PASS_REGULAR_EXPRESSION ${result}) # 为指定测试名设置匹配规则, result:结果匹配的字符串
endfunction(do_test1)

# # do a bunch of result based tests
do_test1(demo 4 5 "2 2.23607")
do_test1(demo 2 4 "1.41421 2")