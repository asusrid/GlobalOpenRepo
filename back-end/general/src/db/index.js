const mongoose = require('mongoose');
const FileModel = require('./file.db');
mongoose.connect('mongodb://localhost:27018/database/globalopenrepo', { useNewUrlParser: true, useFindAndModify: false, useCreateIndex: true, useUnifiedTopology: true})
.then(() => {
	console.log('[MONGODB]: MongoDB Connected');
})
.catch(error => {
	console.log('[MONGODB]: ', error);
});

module.exports = {
	FileModel
};