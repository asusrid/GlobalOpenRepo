const mongoose = require("mongoose");

// schema
const fileSchema = new mongoose.Schema({
    name: { type: String }, //file name.
    location: { type: String }, //server path to file.
    headers: [{ type: String }], //key columns of the file.
    md5: { type: String }
},{collection: 'FileCol', strict: false});

const File = mongoose.model("File", fileSchema, "FileCol");
module.exports = File;