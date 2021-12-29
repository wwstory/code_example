#include <iostream>
#include "nlohmann/json.hpp"

using json = nlohmann::json;

void test1() {
    std::cout << "\n--- 创建json对象" << std::endl;
    json j;
    j["pi"] = 3.141;
    j["data"] = {{"name", "yaomeng"}, {"age", 16}};
    j["followers"] = {"you", "me", "he", "she"};
    std::cout << j << std::endl;

    std::string str = j.dump();  // json对象转为string
    std::cout << str << std::endl;

    json j2 = {{"pi", 3.141},
               {"happy", true},
               {"name", "Niels"},
               {"nothing", nullptr},
               {"answer", {{"everything", 42}}},
               {"list", {1, 0, 2}},
               {"object", {{"currency", "USD"}, {"value", 42.99}}}};
    std::cout << j2 << std::endl;
}

void test2() {
    std::cout << "\n--- 明确指明数组/对象" << std::endl;
    // a way to express the empty array []
    json empty_array_explicit = json::array();

    // ways to express the empty object {}
    json empty_object_implicit = json({});
    json empty_object_explicit = json::object();

    // a way to express an _array_ of key/value pairs [["currency", "USD"],
    // ["value", 42.99]]
    json array_not_object =
        json::array({{"currency", "USD"}, {"value", 42.99}});

    std::cout << empty_array_explicit << std::endl;
    std::cout << empty_object_implicit << std::endl;
    std::cout << empty_object_explicit << std::endl;
    std::cout << array_not_object << std::endl;
}

void test3() {
    std::cout << "\n--- To/From 字符串" << std::endl;
    json j = "{ \"happy\": true, \"pi\": 3.141 }"_json;
    std::cout << j << std::endl;

    auto j2 = R"(
    {
        "happy": true,
        "pi": 3.141
    }
    )"_json;
    std::cout << j2 << std::endl;

    // parse explicitly
    auto j3 = json::parse(R"({"happy": true, "pi": 3.141})");
    std::cout << j3 << std::endl;

    // explicit conversion to string
    std::string s = j.dump();             // {"happy":true,"pi":3.141}
    std::cout << j.dump(4) << std::endl;  // dump参数indent设置空格
}

void test4() {
    std::cout << "\n--- 其它：类型转换" << std::endl;
    // store a string in a JSON value
    json j_string = "this is a string";

    // retrieve the string value
    auto cpp_string = j_string.get<std::string>();
    // retrieve the string value (alternative when an variable already exists)
    std::string cpp_string2;
    j_string.get_to(cpp_string2);

    std::cout << j_string << std::endl;
    std::cout << cpp_string << std::endl;
    std::cout << cpp_string2 << std::endl;
}

int main(int, char**) {
    test1();
    test2();
    test3();
    test4();

    return 0;
}
