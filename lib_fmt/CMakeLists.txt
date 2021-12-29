cmake_minimum_required(VERSION 3.0.0)
project(demo VERSION 0.1.0)

include(CTest)
enable_testing()

add_executable(demo main.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)

# doc: https://fmt.dev/latest/usage.html
add_subdirectory(fmt)
# add_subdirectory(fmt EXCLUDE_FROM_ALL)    # EXCLUDE_FROM_ALL: 编译后剔除

target_link_libraries(demo fmt)
# target_link_libraries(demo fmt-header-only)   # 仅是fmt提供了fmt-header-only，可以将目标设置为仅使用header的版本
