const mongoose = require('mongoose');

mongoose.connect('mongodb://database/globalopenrepo', { useNewUrlParser: true, useFindAndModify: false, useCreateIndex: true, useUnifiedTopology: true})
.then(() => {
	console.log('[MONGODB]: MongoDB Connected');
})
.catch(error => {
	console.log('[MONGODB]: ', error);
});

module.exports = {

};