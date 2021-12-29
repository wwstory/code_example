add_library(math_func my_sqrt.cc)

install(TARGETS math_func DESTINATION lib)          # 安装  将(TARGETS)二进制文件math_func放入bin目录
install(FILES math_func.h DESTINATION include)      # 安装  将(FILES)头文件math_func.h放入include目录