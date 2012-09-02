
var fs      = require('fs');
var path    = require('path');

var _       = require('underscore');
var winston = require('winston');

var reverse = require('ascii-art-reverse');

var animals = ['almost there!'];
var ANIMALS_PATH = path.join(__dirname, '../public/assets/animals.saved');
var SEPERATOR = '===============++++SEPERATOR++++====================\n';

winston.info('Loading animals file ...');

var equalizePadding = function (animal) {

    var lines = animal.replace(/\r/g, '').split('\n');

    var max = _.max(_.map(lines, function (line) { return line.length; }));
    lines = _.map(lines, function (line) {
        var paddingLength = max - line.length;
        var paddingStr = '';
        _.each(_.range(paddingLength), function () { paddingStr += ' '; });
        return line + paddingStr;
    });

    return lines.join('\n');
};

fs.readFile(ANIMALS_PATH, 'utf8', function (err, data) {
    if (err) throw err;

    winston.info('Loaded animals file.');

    var animalStr = data.toString();

    animals = [];

    animals = _.map(animalStr.split(SEPERATOR), function (animal) {
        return equalizePadding(animal);
    });

    winston.info('Loaded ' + animals.length + ' animals.');
});

var offsetAnimal = function (animal, offset) {

    var offsetStr = '';
    _.each(_.range(offset), function () { offsetStr += ' '; });

    var lines = animal.replace(/\r/g, '').split('\n');
    lines = _.map(lines, function (line) {
        return offsetStr + line;
    });

    return lines.join('\n');
};

var reverseAnimal = function (animal) {
    // Thanks to github.com/regality
    // https://github.com/regality/ascii-art-reverse
    return reverse(animal);
};

exports.getAll = function () {
    return animals;
};

exports.get = function (index, offset, reverse) {

    var animal = animals[index];

    if (reverse) animal = reverseAnimal(animal);
    if (offset > 0) animal = offsetAnimal(animal, offset);

    return animal;
};

exports.dimensions = function (animal) {

    var lines = animal.replace(/\r/g, '').split('\n');

    var width = _.max(_.map(lines, function (line) { return line.length; }));

    return {
        width: width,
        height: lines.length
    };
};