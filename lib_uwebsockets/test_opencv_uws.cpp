#include <iostream>
#include <opencv2/opencv.hpp>
#include <vector>
#include "uWebSockets/App.h"

const int _PORT = 3000;

int main(){
    std::vector<std::string> image_paths {
        "./res/1.jpg",
        "./res/2.jpg",
        "./res/3.jpg",
        "./res/4.jpg",
    };

    std::cout << "hello world" << std::endl;
    std::cout << CV_VERSION << std::endl;
    cv::Mat image;

    for(std::string image_path : image_paths){
        image = cv::imread(image_path, 1);
        cv::imshow("display", image);
        cv::waitKey(1000);
    }
    cv::destroyAllWindows();

    uWS::App app = uWS::App();

    struct PerSocketData {
        /* Fill with user data */
    };
    app.ws<PerSocketData>("/msg", {
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
			std::cout << "A client has connected" << std::endl;
			ws->subscribe("broadcast");
            ws->publish("broadcast", "A new user has joined");
        },
        // .message = [&app](auto *ws, std::string_view message, uWS::OpCode opCode) {  // broadcast need app send
        .message = [](auto *ws, std::string_view message, uWS::OpCode opCode) {
            std::cout << "Message: " << message << std::endl;
            // ws->send(message, opCode, true);
            // app.publish("broadcast", message, opCode);   // broadcast need app send
            ws->publish("broadcast", message, opCode);
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
    }).run();


    return 0;
}
