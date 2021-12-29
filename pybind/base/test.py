# %%
# 默认的cmake生成库，会在名字前面添加lib，导致与demo.cpp里面PYBIND11_MODULE的第一个参数不同，从而无法导入。
# 可以手动将libdemo.so改成demo.so
from build.demo import add

print(add(1, 3))

# %%
