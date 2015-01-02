var koa = require('koa');
var animals = require('./lib/animals');
var app = koa();
var bodyParser = require('koa-bodyparser');
var logger = require('koa-logger')

/**
 * Exports.
 */

module.exports = app;

/**
 * Middleware.
 */

app.use(bodyParser());
app.use(logger());

/**
 * Load an animal at /.
 */

app.use(function *(){
  var index = integer(this.query.index, 0, animals.length);
  var maxWidth = integer(this.query.maxwidth, 10, 1000);
  var maxHeight = integer(this.query.maxHeight, 10, 1000);
  var offset = integer(this.query.offset, 0, 1000);
  var reverse = this.query.reverse === 'true';
  var terminal = this.query.terminal === 'true';

  // select the animal
  var animal = select(index, maxWidth, maxHeight);
  if (reverse) animal = animals.reverse(animal);
  if (offset) animal = animals.offset(animal, offset);

  // output as many deletion characters as the animal
  if (terminal) {
    var dims = animals.dimensions(animal);
    var ansi = '';
    for (var i = 0; i < dims.height-1; i += 1)
      animal = '\x1b[2K\r' + '\x1b[1F' + animal;
  }

  this.type = 'text/plain; charset=utf-8';
  this.body = animal;
});

/**
 * Parse an integer input.
 */

function integer(str, min, max) {
  if (str && parseInt(str) >= min && parseInt(str) < max) 
    return parseInt(str);
  else 
    return null;
}

/**
 * Select the animal.
 * @param  {Number} index  Animal index to select
 * @param  {Number} width  Max width
 * @param  {Number} height max height
 * @return {String}        Selected animal
 */

function select(index, width, height) {
  if (index) return animals[index];
  // if we have width or height criteria, select it
  if (width || height) {
    for (var i = 0; i < animals.length; i += 1) {
      var animal = animals[i];
      var dims = animals.dimensions(animal);
      if (width && dims.width > width) continue;
      if (height && dims.height > height) continue;
      return animal;
    }
  }
  return animals[Math.floor(Math.random() * animals.length)];
}

