#include "rapidjson/document.h"
#include "rapidjson/writer.h"
#include "rapidjson/stringbuffer.h"
#include <iostream>

void test1(){
    std::cout << "\n--- 解析为obj并修改数据，再转换为string:" << std::endl;

    // 1. 把 JSON 解析至 DOM
    std::string str_json = R"({"project": "demo", "data": {"name": "maple", "lv": 1018}, "favor": ["like", "fast"], "stars": 10})";
    rapidjson::Document doc;
    doc.Parse(str_json.c_str());
    // const char* char_json = "{\"project\": \"demo\", \"data\": {\"name\": \"maple\", \"lv\": 1018}, \"favor\": [\"like\", \"fast\"], \"stars\": 10}";
    // rapidjson::Document doc;
    // doc.Parse(char_json);

    // 2. 利用 DOM 作出修改
    rapidjson::Value &s = doc["stars"];
    s.SetInt(s.GetInt() + 1);

    // 3. 把 DOM 转换（stringify）成 JSON
    rapidjson::StringBuffer buffer;
    rapidjson::Writer<rapidjson::StringBuffer> writer(buffer);
    doc.Accept(writer);

    std::cout << buffer.GetString() << std::endl;
}

void test2(){
    std::cout << "\n--- 操作数组、字典:" << std::endl;

    // 1. 把 JSON 解析至 DOM
    std::string str_json = R"({"project": "demo", "data": {"name": "maple", "lv": 1018}, "favor": ["like", "fast"], "stars": 10})";
    rapidjson::Document doc;
    doc.Parse(str_json.c_str());
    // const char* char_json = "{\"project\": \"demo\", \"data\": {\"name\": \"maple\", \"lv\": 1018}, \"favor\": [\"like\", \"fast\"], \"stars\": 10}";
    // rapidjson::Document doc;
    // doc.Parse(char_json);

    // 2. 利用 DOM 作出修改
    rapidjson::Value &s = doc["stars"];
    s.SetInt(s.GetInt() + 1);

    std::cout << s.GetInt() << std::endl;
    std::cout << doc["data"].GetObj()["name"].GetString() << std::endl;
    std::cout << doc["favor"].GetArray()[0].GetString() << std::endl;
}

int main(int argc, char const *argv[])
{
    test1();

    test2();

    return 0;
}
