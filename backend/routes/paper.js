const express = require("express");
const router = express.Router();

const {
  Model,
  testing,
} = require("../controllers/paper");

router.post("/model", Model);
router.get("/test", testing);

module.exports = router;
