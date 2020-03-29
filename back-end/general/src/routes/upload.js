const express = require('express');
const router = express.Router();
const { FileModel } = require('../db');

/* POST video. */
router.post('/', async (req, res) => {
	if (!req.files || Object.keys(req.files).length === 0) {
	    return res.status(400).send('No files were uploaded.');
	}
	//console.log(req.files.video);
	console.log(req.body.separator);
	// The input field
	let file = req.files.file;
	file.mv('/warehouse/', function(err) {
	    if (err) return res.status(500).send(err);
	    console.log(req.files.file);
	    // ToDo extract headers and save into db
	    res.send(200).json({'message':'okay'});
	});
});

module.exports = router;
