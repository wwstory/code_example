#include <map>
#include <vector>
#include "fmt/color.h"
#include "fmt/os.h"
#include "fmt/ranges.h"

void test1() {
    fmt::print("\n--- 打印集合\n");
    // std::vector<int> v1{1, 2, 3, 4};
    // std::vector<std::vector<int>> v1{{1, 2, 3, 4}, {5, 6}};
    std::vector<std::map<std::string, int>> v1{{{"a", 1}, {"b", 2}},
                                               {{"abc", 10}, {"xyz", 20}}};
    fmt::print("{}\n", v1);
}

void test2() {
    fmt::print("\n--- 输出字符串到文件\n");
    auto out = fmt::output_file("guide.txt");
    out.print("Don't {}", "Panic");
}

void test3() {
    fmt::print("\n--- 带颜色打印\n");
    fmt::print(fg(fmt::color::crimson) | fmt::emphasis::bold, "Hello, {}!\n",
               "world");
    fmt::print(fg(fmt::color::floral_white) | bg(fmt::color::slate_gray) |
                   fmt::emphasis::underline,
               "Hello, {}!\n", "мир");
    fmt::print(fg(fmt::color::steel_blue) | fmt::emphasis::italic,
               "Hello, {}!\n", "世界");
}

int main(int, char**) {
    test1();
    test2();
    test3();
}
