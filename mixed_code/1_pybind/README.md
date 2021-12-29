- demo1: 基础，py调用c++函数
- demo2: 基础，c++调用py模块
- demo3: 基础，py调用c++类
- demo4: c++类传入py对象执行

```sh
# 编译
g++ -shared -fPIC $(python3 -m pybind11 --includes) demo.cpp -o demo$(python3-config --extension-suffix)
```
