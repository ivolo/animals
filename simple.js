
var winston = require('winston');
    server  = require('./server.js');

server.listen(server.port);

winston.info('Site server set to port ' + server.port + '!');
