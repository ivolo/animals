
var path           = require('path');

var express        = require('express');


module.exports = function (app) {

    var publicDirectory = path.join(__dirname, 'public/');

    app.configure('development', function() {
        app.use(express.static(publicDirectory));
        app.use(express.errorHandler({ dumpExceptions: true, showStack: true }));
    });

    app.configure('production', function(){
      var oneYear = 31557600000;
      app.use(express.static(publicDirectory, { maxAge: oneYear }));
      app.use(express.errorHandler());
    });

    app.use(app.router);
};