function greet(name) {
  console.log(`Hello ${name}`);
  greet2(name);
  console.log("Getting ready to say bye...");
  bye();
}

function greet2(name) {
  console.log(`How are you ${name}?`);
}

function bye() {
  console.log("Ok, bye!");
}

greet("Farshad");
