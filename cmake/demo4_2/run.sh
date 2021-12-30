#!/bin/sh

cd src
if [ -d build ]; then
    rm -r build
fi
mkdir build
cd build
cmake ..
make
./demo
