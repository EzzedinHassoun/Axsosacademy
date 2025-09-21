
var isPalindrome = function(x) {
    
    if (x < 0) {
        return false;
    }

    const strX = x.toString();

    const reversedStrX = strX.split('').reverse().join('');

    return strX === reversedStrX;
};