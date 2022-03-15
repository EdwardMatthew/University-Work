// Program to showcase the map, filter, and reduce functions
// map is used to create a new array from an existing array
// filter applies a conditional statement to each element in the array
// reduce reduces an array to just one value

const food = ["bacon", "lettuce", "apple"];

// Map example
function category(food) {
    if (food == "bacon") {
        return "meat";
    } else if (food == "lettuce") {
        return "veggie";
    } else if (food == "apple") {
        return "fruit";
    }
}

const type = food.map(item => console.log(category(item)));

// filter example (filter out the even numbers, leaving the odd numbers)
const numbers = [1,2,3,4,5];
const odd = numbers.filter(value => value % 2 != 0);
console.log(odd);

// reduce example (multiply every number in the array, thereby reducing the array)
const total = numbers.reduce(function (result, item) {
    return result * item;
});

console.log(total);