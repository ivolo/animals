
var winston = require('winston');
    server  = require('./server.js');

var port = process.env.PORT || server.port;

server.listen(port);

winston.info('Site server set to port ' + port + '!');
