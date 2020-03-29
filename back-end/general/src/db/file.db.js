const mongoose = require("mongoose");

// schema
const fileSchema = new mongoose.Schema({
    name: { type: String }, //file name.
    location: { type: String }, //server path to file.
    fields: [{ type: String }] //key columns of the file.
},{collection: 'FileCol'});

const File = mongoose.model("File", fileSchema, "FileCol");
module.exports = File;