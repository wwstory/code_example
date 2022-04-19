#include <iostream>
#include <opencv2/opencv.hpp>
#include <vector>
#include <time.h>


uchar * mat_to_bytes(cv::Mat img){
    // img = img.reshape(0, 1);
    int size = img.total() * img.channels();
    uchar* data = new uchar[size];
    std::memcpy(data, img.data, size * sizeof(uchar));
    return data;
}


int main(){

    // cv::Mat img = cv::imread(image_paths[i], cv::IMREAD_COLOR);
    cv::Mat img = cv::imread("./res/1.jpg");

    uchar* data = mat_to_bytes(img);

    // std::cout << *data << std::endl;
    // printf("%d\n", *data);
    for(int i = 0; i < 10; ++i)
        printf("%d\n", *(data+635*425*3-i));
    
    std::cout << "----" << std::endl;
    char* c1 = "abc\0def";
    std::cout << c1 << std::endl;
    std::cout << std::string_view(c1) << std::endl;

    std::cout << "----" << std::endl;
    std::string_view sv1 {c1, 7};   // std::string_view sv1 (c1, 7);
    std::cout << sv1 << std::endl;

    return 0;
}
