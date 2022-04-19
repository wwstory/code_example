#include <iostream>
#include <opencv2/opencv.hpp>


int main(){
    cv::Mat img;
    cv::namedWindow("video play");
    cv::VideoCapture cap(0);

    if(!cap.isOpened()){
        std::cout << "no camera" << std::endl;
        exit(-1);
    }

    while(true){
        cap >> img;
        if(img.empty()){
            break;
        }
        cv::imshow("video play", img);
        char c = (char) cv::waitKey(24);
        if( c == 27){
            break;
        }
    }

    cap.release();

    return 0;
}
