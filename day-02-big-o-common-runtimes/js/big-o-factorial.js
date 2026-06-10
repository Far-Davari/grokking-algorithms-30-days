function factorial(n) {
    if (n < 0) return undefined;
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

function routes(n) {
    if (n < 2) return 0;
    return factorial(n - 1);
}

for (let i = 2; i <= 20; i++) {
    console.log(`${i} cities -> ${routes(i)} routes`);
}