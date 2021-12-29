#include <pybind11/embed.h> // everything needed for embedding
namespace py = pybind11;
using namespace py::literals;

int main() {
    py::scoped_interpreter guard{}; // start the interpreter and keep it alive

    py::print("Hello, World!"); // use the Python API

    py::exec(R"(
        kwargs = dict(name="World", number=42)
        message = "Hello, {name}! The answer is {number}".format(**kwargs)
        print(message)
    )");

    auto kwargs = py::dict("name"_a="World", "number"_a=42);
    auto message = "Hello, {name}! The answer is {number}"_s.format(**kwargs);
    py::print(message);

    // 导入自定义的py代码
    py::module_ sys = py::module_::import("sys");
    sys.attr("path").attr("append")("..");  // 生成的执行文件在build/目录下，而cal.py在build/目录的上级
    py::print(sys.attr("path"));

    py::module_ cal = py::module_::import("cal");
    py::print(cal.attr("val"));
    auto add = cal.attr("add");
    py::print(add(3, 2));
    py::object result = add(3, 2);
    int n = result.cast<int>();

    auto a1 = cal.attr("A")();  // 类
    py::print(a1.attr("func")(10));
}