
var _       = require('underscore');

var animals = require('../lib/animals');



var getNumber = function (req, key) {

    var offset = parseInt(req.param(key), 10);

    if (_.isNaN(offset) || !_.isNumber(offset) || offset < 0 || offset > 1000)
        offset = 0;

    return offset;
};

var chooseUsingDimensions = function (req, index) {

    var len = animals.getAll().length;

    var maxWidth = getNumber(req, 'maxwidth');
    var maxHeight = getNumber(req, 'maxheight');

    if (maxWidth || maxHeight) {

        for (var i = 0; i < len; i += 1) {

            var dims = animals.dimensions(index);
            var satisfied = true;

            if (maxWidth && dims.width > maxWidth) {
                satisfied = false;
            }

            if (maxHeight && dims.height > maxHeight) {
                satisfied = false;
            }

            if (satisfied) break;

            index = (index + 1) % len;
        }
    }

    return index;
};

var getIndex = function (req) {

    var index = parseInt(req.param('index'), 10);

    var len = animals.getAll().length;

    if (_.isNaN(index) || !_.isNumber(index) || index >= len || index < 0)
        index = Math.floor(Math.random() * len);
    else
        index = Math.floor(index);

    return index;
};

var getReverse = function (req) {

    var reverse = req.param('reverse');

    if (_.isString(reverse)) reverse = reverse.toLowerCase();

    reverse = reverse === 'true';

    return reverse;
};


exports.home = function (req, res, next) {

    var index = chooseUsingDimensions(req, getIndex(req));

    var offset = getNumber(req, 'offset');
    var reverse = getReverse(req);

    var animal = animals.get(index, offset, reverse);

    res.set('Content-Type', 'text/plain; charset=utf-8');
    res.send(animal);
};

exports.dimensions = function (req, res, next) {

    var index = getIndex(req);

    res.json(animals.dimensions(index));
};