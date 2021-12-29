#include <iostream>
#include "math_func/math_func.h"

#include <string>

using namespace std;

int main(int argc, char* argv[])
{
    string str1, str2;
    str1 = argv[1];
    str2 = argv[2];
    cout << my_sqrt(stoi(str1)) << " " << my_sqrt(stoi(str2)) << endl;
    return 0;
}