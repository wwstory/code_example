#include <iostream>
#include "hello.h"
#include "HelloConfig.h"
int main()
{
    say("I can say Hello!");
    std::cout << "version:" << demo_VERSION_MAJOR << "." << demo_VERSION_MINOR << std::endl;
    return 0;
}