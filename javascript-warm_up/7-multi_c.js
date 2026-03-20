#!/usr/bin/node

const arg = process.argv[2];
const convertInt = parseInt(arg);
if (isNaN(convertInt)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < convertInt; i++) {
    console.log('C is fun');
  }
}
