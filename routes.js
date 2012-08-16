
var controllers = require('./controllers');

// Shorthand vars for the routes
var animals         = controllers.animals;

module.exports = function (app) {


    app.get('/dimensions/?',   animals.dimensions);
    app.get('/?',              animals.home);


};


