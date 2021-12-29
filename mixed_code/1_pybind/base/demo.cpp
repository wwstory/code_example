#include <pybind11/pybind11.h>

int add(int i, int j) {
    return i + j;
}

// 输出的库名(xxx.so)与此处的第一个参数相同
PYBIND11_MODULE(demo, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("add", &add, "A function which adds two numbers");
}

// 编译
// c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) demo.cpp -o demo$(python3-config --extension-suffix)
// g++ -shared -fPIC $(python3 -m pybind11 --includes) demo.cpp -o demo$(python3-config --extension-suffix)