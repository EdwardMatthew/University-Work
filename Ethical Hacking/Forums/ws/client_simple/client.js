const WebSocket = require('ws');

const ServerAddress = "ws://ec2-54-169-59-250.ap-southeast-1.compute.amazonaws.com/ws/1";

const ws = new WebSocket(ServerAddress)