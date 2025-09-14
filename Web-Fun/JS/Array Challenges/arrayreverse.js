function reverse(arr) {

    for (var i = arr.length; i >= 0; i--) {
        var pointer = arr.length;
        arr[pointer] = arr[i];
        arr.splice(i, 1);
        pointer++;

    }
    return arr;
}

var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); 