#!/usr/bin/node
// prints a square

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    let sq = '';
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      sq += 'X';
    }
    console.log(sq);
  }
}
