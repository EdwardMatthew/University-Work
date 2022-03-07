// Program to explain what the fetch function is
// fetch is a function (technically an API) used for sending a network request regarding multiple things
// aside from sending a network request, fetch can also be used to grab information from JSON files 
// This program fetches the local JSON data, and prints it to the web console

function loadGames(data) {
    var container = document.getElementById("demo");
    for (var i = 0; i < data.length; i++) {
        var p = document.createElement("h3");
        p.innerHTML = `Name: ${data[i].name} <br> Platform: ${data[i].platform}`;
        container.appendChild(p);
    }
}

fetch("games.json").then(response => response.json()).then(data => loadGames(data));
