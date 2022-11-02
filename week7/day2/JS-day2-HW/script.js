//==========Exercise #1 ===========//
/*
Write a function that parses through the below object and displays all of their
favorite food dishes as shown:
*/

let person3 = {
  pizza: ["Deep Dish", "South Side Thin Crust"],
  tacos: "Anything not from Taco bell",
  burgers: "Portillos Burgers",
  ice_cream: ["Chocolate", "Vanilla", "Oreo"],
  shakes: [
    {
      oberwise: "Chocolate",
      dunkin: "Vanilla",
      culvers: "All of them",
      mcDonalds: "Sham-rock-shake",
      cupids_candies: "Chocolate Malt",
    },
  ],
};

for (const property in person3) {
  if (typeof person3[property][0] == "object") {
    console.log("Here come the favorite shakes!");
    for (const property in person3.shakes[0]) {
      console.log(
        `Person3's fav from ${property}: ${person3.shakes[0][property]}`
      );
    }
  } else {
    console.log(`Person3's fav ${property}: ${person3[property]}`);
  }
}

//=======Exercise #2=========//
/*
Write an object prototype for a Person that has a name and age, has a
printInfo method, and also has a method that 
increments the persons age by 1 each time the method is called.
Create two people using the 'new' keyword, and print 
both of their infos and increment one persons
age by 3 years. Use an arrow function for both methods
*/

// Create our Person Prototype
function Person(first, last, age) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;

  // Use an arrow to create the printInfo method
  this.printInfo = () => {
    console.log(`${this.firstName} ${this.lastName} is ${this.age} years old.`);
  };

  // Create another arrow function for the addAge method that takes a single parameter
  // Adding to the age
  this.addAge = (n) => (this.age += n);
}

const p1 = new Person("Brandt", "Carlson", 900);
const p2 = new Person("Shoha", "Tsuchida", 1000);

p1.printInfo();
p1.addAge(3);
p1.printInfo();
p2.printInfo();
p2.addAge(1);
p2.printInfo();

// =============Exercise #3 ============//
/*

    Create a Promised based function that will check a string to determine if it's length is greater than 10.
    If the length is greater than ten console log "Big word". 
    If the length of the string is less than 10 console log "Small Number"
*/

const checkLength = async (str) => {
  let promise = new Promise((resolve, reject) => {
    if (str.length > 10) {
      resolve("Big word");
    } else {
      reject("Small Number");
    }
  });
  try {
    const response = await promise;
    console.log(response);
  } catch (error) {
    console.log(error);
  }
};

checkLength("ThisWasAConfusingOne");

// CODE WARS

// Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
// Example
// createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"
// The returned format must be correct in order to complete this challenge.
// Don't forget the space after the closing parentheses!

function createPhoneNumber(numbers) {
  return (
    "(" +
    numbers[0] +
    numbers[1] +
    numbers[2] +
    ")" +
    " " +
    numbers[3] +
    numbers[4] +
    numbers[5] +
    "-" +
    numbers[6] +
    numbers[7] +
    numbers[8] +
    numbers[9]
  );
}

//   Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.
//   Note: a and b are not ordered!
//   Examples (a, b) --> output (explanation)
//   (1, 0) --> 1 (1 + 0 = 1)
//   (1, 2) --> 3 (1 + 2 = 3)
//   (0, 1) --> 1 (0 + 1 = 1)
//   (1, 1) --> 1 (1 since both are same)
//   (-1, 0) --> -1 (-1 + 0 = -1)
//   (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

function getSum(a, b) {
  var list = [];

  if (a < b) {
    for (var i = a; i <= b; i++) {
      list.push(i);
    }
  } else {
    for (var i = b; i <= a; i++) {
      list.push(i);
    }
  }
  const sum = list.reduce(
    (previousValue, currentValue) => previousValue + currentValue,
    0
  );
  return sum;
}
