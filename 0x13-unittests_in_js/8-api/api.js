const express = require('express');
const app = express();


app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
    console.log('API available on localhost port 7865')
}).listen(7865);

module.exports = app;