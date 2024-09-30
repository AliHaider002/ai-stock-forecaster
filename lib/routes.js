const router = require("express").Router();
const stockRoutes = require("./modules/stocks/stockRoute");

router.use("/stock", stockRoutes);

module.exports = router;
