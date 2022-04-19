#include <iostream>
#include <opencv2/opencv.hpp>
#include <vector>
#include <time.h>
#include "uWebSockets/App.h"

const int _PORT = 3000;

uWS::App *global_app;

std::vector<std::string> image_paths {
    "./res/1.jpg",
    // "./res/2.jpg",   // too big, python websockets rev has problem!
    // "./res/3.jpg",
    // "./res/4.jpg",
    "./res/5.jpg",
    "./res/6.jpg",
    // "./res/7.jpg",
    "./res/8.jpg",
};
uint i = 0;


uchar * mat_to_bytes(cv::Mat& img){
    // img = img.reshape(0, 1);
    int size = img.total() * img.channels();
    uchar* data = new uchar[size];
    memcpy(data, img.data, size * sizeof(uchar));
    return data;
}


int main(){
    uWS::App app = uWS::App();

    struct PerSocketData {
        /* Fill with user data */
    };
    app.ws<PerSocketData>("/img", {
        /* Settings */
        .compression = uWS::CompressOptions(uWS::DEDICATED_COMPRESSOR_4KB | uWS::DEDICATED_DECOMPRESSOR),
        .maxPayloadLength = 100 * 1024 * 1024,
        .idleTimeout = 16,
        .maxBackpressure = 100 * 1024 * 1024,
        .closeOnBackpressureLimit = false,
        .resetIdleTimeoutOnSend = false,
        .sendPingsAutomatically = true,
        /* Handlers */
        .upgrade = nullptr,
        .open = [](auto *ws) {
            /* Open event here, you may access ws->getUserData() which points to a PerSocketData struct */
            // PerSocketData *perSocketData = (PerSocketData *) ws->getUserData();

            // std::vector<std::string> image_paths {
            //     "./res/1.jpg",
            //     "./res/2.jpg",
            //     "./res/3.jpg",
            //     "./res/4.jpg",
            // };

            // for(std::string image_path : image_paths){
            //     auto img = std::make_shared<cv::Mat>(cv::imread(image_path, 1));
            //     perSocketData->images.push_back(img);
            // }

			ws->subscribe("img");
            // ws->publish("msg", "A new user has connected");
        },
        // .message = [&app](auto *ws, std::string_view message, uWS::OpCode opCode) {  // broadcast need app send
        .message = [](auto *ws, std::string_view message, uWS::OpCode opCode) {
            // std::cout << "Message: " << message << std::endl;

            // PerSocketData *perSocketData = (PerSocketData *) ws->getUserData();
            // auto image = perSocketData->images.back();
            // ws->publish("img", std::string_view((char *)image->data), uWS::OpCode::BINARY, false);
            // perSocketData->images.pop_back();

            // std::cout << "send img!" << message << ws->getUserData()->images.size() << std::endl;
        },
        .drain = [](auto */*ws*/) {
            /* Check ws->getBufferedAmount() here */
        },
        .ping = [](auto */*ws*/, std::string_view) {
            /* Not implemented yet */
        },
        .pong = [](auto */*ws*/, std::string_view) {
            /* Not implemented yet */
        },
        .close = [](auto */*ws*/, int /*code*/, std::string_view /*message*/) {
            /* You may access ws->getUserData() here */
        }
    });

    app.listen(_PORT, [](auto *listen_socket) {
        if (listen_socket) {
            std::cout << "Listening on port " << _PORT << std::endl;
        }
    });
    
    struct us_loop_t *loop = (struct us_loop_t *) uWS::Loop::get();
    struct us_timer_t *delayTimer = us_create_timer(loop, 0, 0);
    us_timer_set(delayTimer, [](struct us_timer_t */*t*/) {

        cv::Mat img = cv::imread(image_paths[i], cv::IMREAD_COLOR);
        // cv::Mat img = cv::imread(image_paths[i]);

        i = ++i % image_paths.size();
        int w = img.cols;
        int h = img.rows;
        int c = img.channels();

        /* send string */
        // global_app->publish("img", "counter: " + std::to_string(i),  uWS::OpCode::TEXT, false);
        /* send mat img */
        uchar* data = mat_to_bytes(img);
        std::string_view send_data = std::string_view((char*)data, w*h*c);  // solve problem: char is \0
        global_app->publish("img", send_data, uWS::OpCode::BINARY, false);

        // cv::Mat img2 = cv::Mat(w, h, CV_8UC2, buff.data());
        // cv::imshow("xxx", img2);
        // cv::waitKey(1000);
        
        std::cout << "send image! " << "size: " << send_data.length() << "=" << img.cols << "*" << img.rows << "*" << img.channels() << std::endl;
    }, 3000, 3000);

    global_app = &app;
    
    app.run();

    return 0;
}
