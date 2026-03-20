#!/usr/bin/node

const arg = process.argv[2];
const convertInt = parseInt(arg);

if (isNaN(convertInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convertInt}`);
}
