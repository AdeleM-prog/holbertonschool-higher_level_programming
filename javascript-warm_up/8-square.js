#!/usr/bin/node

const sqSize = parseInt(process.argv[2]);
if (isNaN(sqSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sqSize; i++) {
    let str = '';
    for (let j = 0; j < sqSize; j++) {
      str = str + 'X';
    }
    console.log(str);
  }
}
