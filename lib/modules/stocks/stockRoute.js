const router = require("express").Router();
const { spawn } = require("child_process");
const { collectData } = require("./stockFacade");

router.get("/", async (req, res) => {
  try {
    res.status(200).json({ message: "Successfully Executed..." });
  } catch (error) {
    res.status(500).json({ message: "Something went wrong", error });
  }
});

router.get("/collect_data", async (req, res) => {
  try {
    const data = await collectData();
    res.status(200).json({ message: "Successfully Collected data...", data });
  } catch (error) {
    res.status(500).json({ message: "Something went wrong", error });
  }
});

router.get("/detector", async (req, res) => {
  try {
    const data = await newsDetector();
    res
      .status(200)
      .json({ message: "Successfully Collected Scraped data...", data });
  } catch (error) {
    res.status(500).json({ message: "Something went wrong", error });
  }
});

module.exports = router;
