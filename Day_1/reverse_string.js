function reverseString(str) {
    // Convert the string to an array of characters, reverse it, and join it back into a string
    return str.split('').reverse().join('');
}

let myString = "Hello, World!";
let reversedString = reverseString(myString);

console.log(myString);       // Original string is unchanged: "Hello, World!"
console.log(reversedString); // Reversed string: "!dlroW ,olleH"
