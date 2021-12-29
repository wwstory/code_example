
[ref](https://pybind11.readthedocs.io/en/stable/upgrade.html?highlight=init#stricter-compile-time-error-checking)

```sh
cd build
cmake ..
make

python3 test.py
```

- 可`CMakeLists.txt`改为生成执行文件，且`demo.cpp`去掉main函数注释，注释PYBIND11_MODULE。`cp build/demo .; ./demo`
- 也可保持输出动态库，python调用。`python3 test.py`