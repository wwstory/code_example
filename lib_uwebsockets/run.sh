#!/bin/sh

run(){
    make test
}

install(){
    apt install libopencv-dev
}


case $1 in
    install)
        install
        ;;
    *)
        run
        ;;
esac
