const express = require('express');
const bodyParser = require('body-parser');
require("./db");
const routes = require('./routes');
const fileUpload = require('express-fileupload');
const helmet = require('helmet');

// add routes

const app = express();
const port = 3000;

// Security protection
app.use(helmet());

// Parsers for POST data
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

// Cross Origin middleware
app.use(function(req, res, next) {
	res.setHeader('Access-Control-Allow-Origin', '*');
	res.setHeader('Access-Control-Allow-Methods', 'GET,HEAD,OPTIONS,POST,PUT,DELETE');
	res.setHeader('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, x-client-key, x-client-token, x-client-secret, Authorization'); // Content-Type
	res.setHeader('Access-Control-Allow-Credentials', true);
	next();
});

app.use(fileUpload());

// Create an HTTP server to run our application
var server = app.listen(port, () => {
    console.log('Application port: ' + port);
});