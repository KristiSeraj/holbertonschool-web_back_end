const express = require('express');
const app = express();

app.use(express.json())

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
    console.log('API available on localhost port 7865')
}).listen(7865);

app.get('/cart/:id(\\d+)', (req, res) => {
    res.send(`Payment methods for cart ${req.params.id}`)
    console.log('API available on localhost port 7865')
})

app.get('/available_payments', (req, res) => {
    res.send({"payment_methods":{"credit_cards":true,"paypal":false}})
    console.log('API available on localhost port 7865')
})


app.post('/login', (req, res) => {
    const username = req.body.userName;
    res.send(`Welcome ${username}`);
    console.log('API available on localhost port 7865')
})

module.exports = app;