const express = require('express');
const router = express.Router();
const uploadRoutes = require('./upload');

router.get('/', (req, res) => {
	res.status(200).json({message: 'Active'});
});

router.use('/upload', uploadRoutes);

module.exports = router;
