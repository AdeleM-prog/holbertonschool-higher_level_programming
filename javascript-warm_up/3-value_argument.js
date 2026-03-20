#!/usr/bin/node
const arg = process.argv2;
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
