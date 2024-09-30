// db.js
const mongoose = require("mongoose");
require("dotenv").config();

const connectDB = async () => {
  try {
    MONGODB_USER = process.env.MONGODB_USER;
    MONGODB_PASSWORD = process.env.MONGODB_PASSWORD;
    const uri = `mongodb+srv://${MONGODB_USER}:${MONGODB_PASSWORD}@stock.l8hbm.mongodb.net/?retryWrites=true&w=majority&appName=stock`;
    await mongoose.connect(uri, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log("MongoDB connected successfully");
  } catch (error) {
    console.error("MongoDB connection error:", error);
    process.exit(1); // Exit process with failure
  }
};

module.exports = connectDB;
