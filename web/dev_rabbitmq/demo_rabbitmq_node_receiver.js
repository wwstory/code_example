#!/usr/bin/env node
// https://www.rabbitmq.com/tutorials/tutorial-one-javascript.html

var amqp = require('amqplib/callback_api');
// amqp.connect('amqp://localhost', function(error0, connection) {
amqp.connect({ protocol: 'amqp', hostname: '192.168.2.13', username: 'user', password: 'password' }, function (error0, connection) {
  if (error0) {
    throw error0;
  }
  connection.createChannel(function (error1, channel) {
    if (error1) {
      throw error1;
    }
    var queue = 'hello';

    channel.assertQueue(queue, {
      durable: false
    });

    console.log(" [*] Waiting for messages in %s. To exit press CTRL+C", queue);
    channel.consume(queue, function (msg) {
      console.log(" [x] Received %s", msg.content.toString());
    }, {
      noAck: true
    });

  });
});

// run:
// node demo_rabbitmq_node_receiver.js