var fs = require('fs');
var max = require('lodash').max;
var reverse = require('ascii-art-reverse');
var path = require('path');

/**
 * Load the animals.
 */

var filepath = path.join(__dirname, '../data/animals.txt');
var animals = fs.readFileSync(filepath).toString();
var sep = '===============++++SEPERATOR++++====================\n';
animals = animals.split(sep).map(pad);

/**
 * Exports.
 */

module.exports = exports = animals;
exports.pad = pad;
exports.offset = offset;
exports.dimensions = dimensions;
exports.reverse = reverse;

/**
 * Pad each line of the animal to be equal length
 * @param  {String} animal The multi line string of the animal
 * @return {String}        padded animal string
 */

function pad(animal) {
  var lines = animal.replace(/\r/g, '').split('\n');
  var width = max(lines, function (line) { return line.length; }).length;
  for (var i = 0; i < lines.length; i += 1) {
    var padding = '';
    for (var x = 0; x < width - lines[i].length; x += 1) padding += ' ';
    lines[i] += padding;
  }
  return lines.join('\n');
}

/**
 * Offset the animal by `spaces`.
 * @param  {String} animal The multi line string of the animal
 * @param  {Number} chars  how many spaces to offset by
 * @return {String}        offset animal string
 */

function offset(animal, spaces) {
  var lines = animal.replace(/\r/g, '').split('\n');
  var str = '';
  for (var i = 0; i < spaces; i += 1) str += ' ';
  for (var i = 0; i < lines.length; i += 1) lines[i] = str + lines[i];
  return lines.join('\n');
}

/**
 * Get the dimensions of the `animal`.
 * @param  {String} animal The multi line string of the animal
 * @return {Object}        Dimensins object with height and width
 */

function dimensions(animal) {
  var lines = animal.replace(/\r/g, '').split('\n');
  var width = max(lines, function (line) { return line.length; }).length;
  return { width: width, height: lines.length };
}

