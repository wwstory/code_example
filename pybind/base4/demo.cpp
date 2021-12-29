#include <pybind11/embed.h> // everything needed for embedding
namespace py = pybind11;
using namespace py::literals;


class __attribute__ ((visibility("hidden"))) B{	// __attribute__设置后，去掉warn
public:
    py::object a;
    B() = default;
    B(py::object a1): a(a1){    // 拷贝
        py::print(a1.attr("func")(10));
    }
    void go(){
        py::print(a.attr("func")(20));
    }
};

// 1 直接运行
// int main() {
//     py::scoped_interpreter guard{};
//     auto a1 = py::module_::import("cal").attr("A")();
//     B b1(a1);
//     return 0;
// }

// 2 作为库
PYBIND11_MODULE(demo, m){
    py::class_<B>(m, "B")
        .def(py::init<py::object &>())
        .def("go", &B::go);
}
