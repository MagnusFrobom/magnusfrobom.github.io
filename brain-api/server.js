const express = require('express');
// const bodyParser = require('body-parser'); // latest version of exressJS now comes with Body-Parser!
const bcrypt = require('bcrypt-nodejs');
const cors = require('cors');
const knex = require('knex');
const Clarifai = require('clarifai');
const register = require('./controllers/register');
const signin = require('./controllers/signin');
const profile = require('./controllers/profile');
const image = require('./controllers/image');

const db = knex({
  // Enter your database information here
  client: 'pg', // PostGres  
  connection: {
    host : '127.0.0.1',
    user : 'magnus',
    password : '',
    database : 'brain'
  }
});


const app = express();

app.use(cors())
app.use(express.json()); // latest version of exressJS now comes with Body-Parser!

// Test only - when you have a database variable you want to use
// app.get('/', (req, res)=> {
//   res.send(database.users);
// })

app.get('/', (req, res) => { res.send(db.users)})
app.post('./controllers/signin', (req, res) => {signin.handleSignin(req, res, db, bcrypt)})
app.post('./controllers/register.js', (req, res) => {register.handleRegister(req, res, db, bcrypt )})
app.get('/profile/:id', (req, res) => {profile.handleProfileGET(req, res, db, bcrypt)})
app.put('/image', (req, res) => { image.handleImage(req ,res)})
app.post('/imageurl', (req, res) => { image.handleApiCall(req, res) })

app.listen(3000, () => {
  console.log('app is running on port 3000');
})
