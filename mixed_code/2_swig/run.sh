#!/bin/sh

if [ -d build ]; then
    rm -r build
fi
mkdir build
cd build
cp -r ../example.* .
cp -r ../*.py .

swig -c++ -python example.i
python3 setup.py build_ext --inplace
g++ -fPIC -c example.cpp
g++ -fPIC -c example_wrap.cxx -I/usr/include/python3.8
g++ -shared example.o example_wrap.o -o _example.so

python3 test.py
