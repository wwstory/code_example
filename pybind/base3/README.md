
[ref](https://pybind11.readthedocs.io/en/stable/advanced/classes.html)

```sh
cd build
cmake ..
make

python3 test.py
```

- demo_1.cpp: 不应该允许构建纯虚函数；为了在python中能扩展抽象类Animal，需要增添和修改部分代码。（Dog不需要额外代码）
