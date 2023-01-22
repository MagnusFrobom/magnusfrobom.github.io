const express = require('express');

const app = express();

const database = {
    users: [
        {
            id: '123',
            name: 'John',
            email: 'john@gmail.com',
            password: 'cookies',
            entries: 0,
            joined: new Date(),
        },
        {
            id: '124',
            name: 'Magnus',
            email: 'frobom.magnus@gmail.com',
            password: 'frobom',
            entries: 0,
            joined: new Date(),
        },
    ]
}

app.get('/', (req, res) => {
    res.send('Its working!');
})

app.post('/signin', (req, res) => {
    if (req.body.email === database.users[0].email &&
        req.body.password === database.users[0].password) {
    res.json('Success');
    } else {
        res.status(400).json('error loging in');
    }
})


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