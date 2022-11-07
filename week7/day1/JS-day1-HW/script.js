/* Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.*/

function disemvowel(str) {
    const answer = str.replace(/[aeiouAEIOU]/g, '');
    return answer;
  }

/*
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b keeping their order.
arrayDiff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:
arrayDiff([1,2,2,2,3],[2]) == [1,3]
 */

function arrayDiff(a, b) {
    var empty = [];
    if (a.length){
    return a.concat(b).filter(item => !a.includes(item) || !b.includes(item));
}
  else {
    return empty;
  }
}

//==================Exercise #1 ==========//
/*Write a function that takes in the string and the list of dog names, loops through 
the list and checks that the current name is in the string passed in. The output should be:
"Matched dog_name" if name is in the string, if no matches are present console.log "No Matches"
*/
let dog_string = "Hello Max, my name is Dog, and I have purple eyes!"
let dog_names = ["Max","HAS","PuRple","dog"]

function findWords(str, li){
    let matches = 0;
    for (let i = 0; i < li.length; i++) {
      if (str.toLowerCase().includes(li[i].toLowerCase())) {
        matches += 1
        console.log(`Matched ${li[i]}`)
      }
      if (matches === 0) {
        console.log('No Matches.')
      }      
    }
};

//Call method here with parameters
findWords(dog_string, dog_names);

//============Exercise #2 ============//
/*Write a fucntion that takes in an array and removes every even index with a splice,
and replaces it with the string "even index" */

// Given arr == ["Max","Baseball","Reboot","Goku","Trucks","Rodger"]

function replaceEvens(arr){
  for (let i = 0; i < arr.length; i++) {
    if (i % 2 === 0) {
      arr.splice(i, 1, "even index")
    }    
  }
  console.log(arr)
};

replaceEvens(["Max","Baseball","Reboot","Goku","Trucks","Rodger"])

//Expected output
//Given arr == ["Max","Baseball","Reboot","Goku","Trucks","Rodger"]
//Output arr == ["even index","Baseball","even index","Goku","even index","Rodger"]