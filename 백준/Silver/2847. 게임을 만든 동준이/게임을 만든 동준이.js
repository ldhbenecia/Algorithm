const fs = require('fs');

function solve(scores) {
  let count = 0;

  for (let i = n - 1; i > 0; i--) {
    if (scores[i] <= scores[i - 1]) {
      let minus_value = scores[i - 1] - scores[i] + 1;
      count += minus_value;
      scores[i - 1] = scores[i] - 1;
    }
  }

  return count;
}

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const n = parseInt(input[0]);
const scores = input.slice(1).map(Number);

const result = solve(scores);
console.log(result);