// Program to explain what Promise, async, await functions
// an async function returns a Promise object, which links to pieces of code together
// await functions wait for a code execution to be finished regardless of the state before executing

// Program to detect saying hello
function sayHello(greetings) {
    return new Promise((resolve, reject) => {
        if (greetings == "Hello") {
            resolve("Hello!");
        } else {
            reject("That is not a greeting");
        }
    });
}


function processHello(response) {
    return new Promise((resolve) => {
        console.log("Processing Greetings");
        resolve(`Extra Information + ${response}`)
    });
}

async function sayHelloBack() {
    const response = await sayHello("Hello");
    console.log("Greetings Received");
    const reply = await processHello(response);
    alert(reply);
}

sayHelloBack();