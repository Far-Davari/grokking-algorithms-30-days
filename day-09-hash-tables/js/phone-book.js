const phoneBook = {};

phoneBook["Jenny"] = 8675309;
phoneBook["Hector"] = 6985464;

console.log(phoneBook["Jenny"]);
console.log(phoneBook["Unknown"]);

const voted = {};
function checkVoter(name) {
  if (voted[name]) {
    console.log("Kicked them out!");
  } else {
    voted[name] = true;
    console.log("Let them vote!");
  }
}

checkVoter("tom");
checkVoter("mike");
checkVoter("tom");
