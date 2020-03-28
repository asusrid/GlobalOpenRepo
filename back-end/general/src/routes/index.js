const express = require('express');
const router = express.Router();

/* POST video. */
router.post('/videos', async (req, res) => {
	if (!req.files || Object.keys(req.files).length === 0) {
	    return res.status(400).send('No files were uploaded.');
	}
	//console.log(req.files.video);

	// The input field
	let classVideo = req.files.video;
	res.send(200).json({'message':'okay'});
});

module.exports = router;
