var express           = require('express');
var http              = require('http');

var routes            = require('./routes');
var setup             = require('./setup');

// increase the max concurrent sockets that the agent can use
http.globalAgent.maxSockets = 2000;

// create the server
var app = express();
// create the http server
var server = http.createServer(app);


// setup global middleware, stylus, etc
setup(app);

// install the routes
routes(app);

server.port = 80;

// export the server for UP
module.exports = server;