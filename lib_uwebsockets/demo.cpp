#include <iostream>
#include <opencv2/opencv.hpp>
#include <vector>
#include <time.h>
#include "uWebSockets/App.h"

#include <opencv2/opencv.hpp>
#include<opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>

#include <vector>
#include <string>

using namespace std;
using namespace cv;

#ifndef CONVERTIMAGE_H_
#define CONVERTIMAGE_H_

/**
 * Classe que converte as imagens para base64 e virse e versa
 */
class ImagemConverter {
public:
	/**
	 * Constritor default da classe
	 */
	ImagemConverter();
	
	/**
	 * Método que converte uma imagem base64 em um cv::Mat
	 * @param imageBase64, imagem em base64
	 * @return imagem em cv::Mat
	 */
	cv::Mat str2mat(const string& imageBase64);
	
	/**
	 * Método que converte uma cv::Mat numa imagem em base64
	 * @param img, imagem em cv::Mat
	 * @return imagem em base64
	 */
	string mat2str(const Mat& img);

	virtual ~ImagemConverter();

private:
	std::string base64_encode(uchar const* bytesToEncode, unsigned int inLen);

	std::string base64_decode(std::string const& encodedString);

};

#endif /* CONVERTIMAGE_H_ */

ImagemConverter::ImagemConverter() {} 

static const std::string base64_chars =
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"abcdefghijklmnopqrstuvwxyz"
"0123456789+/";

static inline bool is_base64( unsigned char c ) 
{ 
	return (isalnum(c) || (c == '+') || (c == '/'));
}

std::string ImagemConverter::base64_encode(uchar const* bytes_to_encode, unsigned int in_len) 
{
	std::string ret;

	int i = 0;
	int j = 0;
	unsigned char char_array_3[3];
	unsigned char char_array_4[4];

	while (in_len--) 
	{
		char_array_3[i++] = *(bytes_to_encode++);
		if (i == 3)
		{
			char_array_4[0] = (char_array_3[0] & 0xfc) >> 2;
			char_array_4[1] = ((char_array_3[0] & 0x03) << 4) + ((char_array_3[1] & 0xf0) >> 4);
			char_array_4[2] = ((char_array_3[1] & 0x0f) << 2) + ((char_array_3[2] & 0xc0) >> 6);
			char_array_4[3] = char_array_3[2] & 0x3f;

			for (i = 0; (i <4); i++) 
			{
				ret += base64_chars[char_array_4[i]];
			}
			i = 0;
		}
	}

	if (i) 
	{
		for (j = i; j < 3; j++) 
		{
			char_array_3[j] = '\0';
		}

		char_array_4[0] = (char_array_3[0] & 0xfc) >> 2;
		char_array_4[1] = ((char_array_3[0] & 0x03) << 4) + ((char_array_3[1] & 0xf0) >> 4);
		char_array_4[2] = ((char_array_3[1] & 0x0f) << 2) + ((char_array_3[2] & 0xc0) >> 6);
		char_array_4[3] = char_array_3[2] & 0x3f;

		for (j = 0; (j < i + 1); j++) 
		{
			ret += base64_chars[char_array_4[j]];
		}
		
		while ((i++ < 3)) 
		{
			ret += '=';
		}
	}

	return ret;
}

std::string ImagemConverter::base64_decode(std::string const& encoded_string)
{
	int in_len = encoded_string.size();
	int i = 0;
	int j = 0;
	int in_ = 0;
	unsigned char char_array_4[4], char_array_3[3];
	std::string ret;

	while (in_len-- && (encoded_string[in_] != '=') && is_base64(encoded_string[in_])) 
	{
		char_array_4[i++] = encoded_string[in_]; in_++;

		if (i == 4) 
		{
			for (i = 0; i < 4; i++) 
			{	
				char_array_4[i] = base64_chars.find(char_array_4[i]);
			}

			char_array_3[0] = (char_array_4[0] << 2) + ((char_array_4[1] & 0x30) >> 4);
			char_array_3[1] = ((char_array_4[1] & 0xf) << 4) + ((char_array_4[2] & 0x3c) >> 2);
			char_array_3[2] = ((char_array_4[2] & 0x3) << 6) + char_array_4[3];

			for (i = 0; (i < 3); i++)
			{
				ret += char_array_3[i];
			}

			i = 0;
		}
	}

	if (i) 
	{
		for (j = i; j < 4; j++) 
		{
			char_array_4[j] = 0;
		}
		
		for (j = 0; j < 4; j++) 
		{	
			char_array_4[j] = base64_chars.find(char_array_4[j]);
		}

		char_array_3[0] = (char_array_4[0] << 2) + ((char_array_4[1] & 0x30) >> 4);
		char_array_3[1] = ((char_array_4[1] & 0xf) << 4) + ((char_array_4[2] & 0x3c) >> 2);
		char_array_3[2] = ((char_array_4[2] & 0x3) << 6) + char_array_4[3];

		for (j = 0; (j < i - 1); j++)
		{	
			ret += char_array_3[j];
		}
	}

	return ret;
}

string ImagemConverter::mat2str(const Mat& m)
{
	int params[3] = {0};
	params[0] = IMWRITE_JPEG_QUALITY;
	params[1] = 100;

	vector<uchar> buf;
	bool code = cv::imencode(".jpg", m, buf, std::vector<int>(params, params+2));
	uchar* result = reinterpret_cast<uchar*> (&buf[0]);

	return base64_encode(result, buf.size());

}


Mat ImagemConverter::str2mat(const string& s)
{
	// Decode data
	string decoded_string = base64_decode(s);
	vector<uchar> data(decoded_string.begin(), decoded_string.end());

	cv::Mat img = imdecode(data, IMREAD_UNCHANGED);
	return img;
}

ImagemConverter::~ImagemConverter()
{
	// TODO Auto-generated destructor stub
}


const int _PORT = 3000;

uWS::App *global_app;
cv::VideoCapture cap(0);
cv::Mat img;
ImagemConverter img_converter;


uchar * mat_to_bytes(cv::Mat& img){
    // img = img.reshape(0, 1);
    int size = img.total() * img.channels();
    uchar* data = new uchar[size];
    memcpy(data, img.data, size * sizeof(uchar));
    return data;
}

void mat_to_jpg(const cv::Mat& img, std::vector<uchar>& buf){
    std::vector<int> params(3);
    params[0] = IMWRITE_JPEG_QUALITY;
    params[1] = 90;
    cv::imencode(".jpg", img, buf, params);
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
        // uchar* data = mat_to_bytes(img);
        // std::string_view send_data = std::string_view((char*)data, img.rows*img.cols*img.channels());  // solve problem: char is \0
        // global_app->publish("img", send_data, uWS::OpCode::BINARY, false);

        // std::cout << "send image! " << "size: " << send_data.length() << "=" << img.cols << "*" << img.rows << "*" << img.channels() << std::endl;

        /* send jpg - error */
        int size = img.total() * img.channels();
        std::string data = img_converter.mat2str(img);
        global_app->publish("img", data, uWS::OpCode::BINARY, false);

        std::cout << "send image! " << "size: " << data.length() << "=" << img.cols << "*" << img.rows << "*" << img.channels() << std::endl;

    }, 10, 10);

    global_app = &app;
    
    app.run();

    return 0;
}
