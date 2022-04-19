#include <iostream>
#include <opencv2/opencv.hpp>
#include <vector>
#include <time.h>
#include "uWebSockets/App.h"

const int _PORT = 3000;

uWS::App *global_app;
cv::VideoCapture cap(0);
cv::Mat img;


uchar * mat_to_bytes(cv::Mat& img){
    // img = img.reshape(0, 1);
    int size = img.total() * img.channels();
    uchar* data = new uchar[size];
    memcpy(data, img.data, size * sizeof(uchar));
    return data;
}

void mat_to_base64(cv::Mat& img){
    
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

        cap >> img;
        if(img.empty()){
            return;
        }

        /* send string */
        // global_app->publish("img", "counter: " + std::to_string(i),  uWS::OpCode::TEXT, false);
        /* send mat img */
        uchar* data = mat_to_bytes(img);
        std::string_view send_data = std::string_view((char*)data, img.rows*img.cols*img.channels());  // solve problem: char is \0
        global_app->publish("img", send_data, uWS::OpCode::BINARY, false);

        std::cout << "send image! " << "size: " << send_data.length() << "=" << img.cols << "*" << img.rows << "*" << img.channels() << std::endl;
    }, 10, 10);

    global_app = &app;
    
    app.run();

    return 0;
}
