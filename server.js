const express = require("express");
const cors = require("cors");
const serve = require("express-static");
const routes = require("./lib/routes");
require("dotenv").config();
const connectDB = require("./lib/db");
const app = express();

connectDB()
  .then(() => {
    app.use(cors());
    app.use(express.json());

    app.use("/api/v1", routes);
    app.use(serve("./uploads"));

    app.get("/", (req, res) => {
      try {
        res.status(200).json({ message: "Alpha Market server is running..." });
      } catch (error) {
        res
          .status(500)
          .json({ message: "Alpha Market server is Failed...", error });
      }
    });

    app.listen(process.env.PORT || 8086, () => {
      console.log("Server is running at PORT: ", process.env.PORT || 8086);
    });
  })
  .catch((e) => console.log(e));
