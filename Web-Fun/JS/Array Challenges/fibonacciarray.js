function fibonacciArray(n) {

    var fibonacci = [0, 1];

    for (let i = 2; i < n; i++) {
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
    }
    return fibonacci;
}

var result = fibonacciArray(20);
console.log(result);
