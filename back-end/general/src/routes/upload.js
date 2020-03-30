const express = require('express');
const router = express.Router();
const { FileModel } = require('../db');

/* POST video. */
router.post('/', async (req, res) => {
	if (!req.files || Object.keys(req.files).length === 0) {
	    return res.status(400).json({err:'No files were uploaded.'});
	}
	//console.log(req.files.video);
	console.log(req.body.separator);
	// The input field
	let dataset = req.files.file;
	console.log(req.files.file);
	dataset.mv('/warehouse/'+dataset.name, function(err) {
	    if (err) return res.status(500).json(err);
	    // console.log(req.files.file);
	    // ToDo extract headers and save into db
	    FileModel.findOne({'md5': dataset.md5}, (err, duplicated) => {
	    	if(duplicated) {console.log(duplicated); return res.status(200).json(duplicated);}
		    let buffer = dataset.data.toString('utf8').split('\n');
		    console.log(buffer.length);
		    let headersFile = buffer[0].split(req.body.separator);
		    let dataFile = new Array();
		    for(let i = 0; i<headersFile.length;i++) {
		    	headersFile[i] = headersFile[i].trim();
		    	dataFile.push(new Array());
		    }
		    
		    for(let i = 1; i<buffer.length;i++) {
		    	let line = buffer[i].split(req.body.separator);
		    	if(line.length == headersFile.length) {
			    	for(let j = 0; j<headersFile.length;j++) {
			    		dataFile[j].push(line[j].toString().replace(/[\n\t\r]/g,"").trim());
			    	}
			    }
		    }

		    let inputFile = new FileModel({
		    	name: dataset.name,
	    		location: '/warehouse/',
	    		headers: headersFile,
	    		md5: dataset.md5
		    });
		    for(let i = 0; i<headersFile.length;i++) {
			    inputFile.set(headersFile[i],dataFile[i]);
			}
			console.log(inputFile);
		    inputFile.save((err,data) => {
		    	if (err) return res.status(500).json(err);
		    	console.log(data);
		    	res.status(200).json(data);
		    });
	    });
	});
});
/*file => {
  name: '350147015.csv',
  data: <Buffer 44 61 74 65 2c 4e ... 1339 more bytes>,
  size: 1389,
  encoding: '7bit',
  tempFilePath: '',
  truncated: false,
  mimetype: 'application/vnd.ms-excel',
  md5: '5001ca2916fb465970c89badc2639151',
  mv: [Function: mv]
}*/

module.exports = router;
