const express = require('express');

const app = express();

app.listen(3001, () => {
    console.log('App is running on port 3001');
})


/* 
/ --> res = this is working
/signin --> POST = succes/fail
/register --> POST = user
/profile/:userId --> GET = user
/image --> PUT --> user

*/