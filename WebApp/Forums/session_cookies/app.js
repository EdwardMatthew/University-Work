const express = require('express');
const cookieParser = require('cookie-parser');
const sessions = require('express-session');

const app = express();
const PORT = 4000;

// express sessions options
const oneDay = 1000 * 60 * 60 * 24;
app.use(sessions({
  secret: "thisismysecrctekeyfhrgfgrfrty84fwir767",
  saveUninitialized: true,
  cookie: { maxAge: oneDay },
  resave: false
})); 

// parse incoming data 
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// serving public file 
app.use(express.static(__dirname));

// cookie parser middleware
app.use(cookieParser());

// auth credentials
const myusername = "Edward";
const mypassword = "mypassword";

// variable to save session
var session;

// adding endpoints
app.get('/', (req, res)=> {
  session = req.session;
  if(session.userid) {
    res.send("Welcome user <a href=\'/logout'>click to logout</a>")
  } else
    res.sendFile('views/index.html', {root:__dirname})
});

app.post('/user', (req, res)=> {
  if (req.body.username == myusername && req.body.password == mypassword) {
    session = req.session;
    session.userid = req.body.username;
    console.log(req.session);
    res.send(`Hey there, welcome <a href=\'/logout'>click to logout</a>`)
  } else {
    res.send("Invalid username or password");
  }
})

app.get('/logout', (req, res) => {
  req.session.destroy();
  res.redirect('/');
});

app.listen(PORT, () => console.log(`Server running at port ${PORT}`));
