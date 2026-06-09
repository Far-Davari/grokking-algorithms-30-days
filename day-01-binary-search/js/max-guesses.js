function maxGuesses(n) {
  if (n < 0) return undefined;
  if (n === 0) return 0;
  if (n === 1) return 1;
  return Math.ceil(Math.log2(n));
}

console.log(maxGuesses(1024));
console.log(maxGuesses(100));
console.log(maxGuesses(0));
console.log(maxGuesses(-1));
