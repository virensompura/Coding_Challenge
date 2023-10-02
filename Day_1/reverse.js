function reverseArray(arr) {
    let reversed = [];
    for (let i = arr.length - 1; i >= 0; i--) {
        reversed.push(arr[i]);
    }
    return reversed;
}

let myArray = [1, 2, 3, 4, 5];
let reversedArray = reverseArray(myArray);

console.log(myArray);       // Original array is unchanged: [1, 2, 3, 4, 5]
console.log(reversedArray); // Reversed copy: [5, 4, 3, 2, 1]

