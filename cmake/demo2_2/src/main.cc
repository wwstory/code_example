#include <iostream>
#include "demo_config.h"

// #include "math_func/math_func.h"
#ifdef USE_MY_MATH  // 来自demo_config.h中的定义，而demo_config.h来自demo_config.h.in，二demo_config.h.in来自CMakeLists中定义
    #include "math_func/math_func.h"
#else
    #include <cmath>
#endif

using namespace std;

int main()
{
#ifdef USE_MY_MATH
    cout << my_sqrt(4.) << " " << my_sqrt(5.) << endl;
#else
    cout << sqrt(4.) << " cmath " << sqrt(5.) << endl;
#endif
    return 0;
}