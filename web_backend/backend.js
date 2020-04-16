/* Set up the server ***************************************************** */
const express = require("express");
const BodyParser = require("body-parser");
const cors = require("cors");
const path = require("path");
const axios = require("axios");
const http = require("http");
const utils = require("./utils");
var zmq = require("zeromq");

var app = express();

app.use(BodyParser.json());
app.use(BodyParser.urlencoded({ extended: true }));
app.use(cors());

const port = process.env.PORT || 5000;

app.listen(port, () => console.log(`Listening on port ${port}`));

/* Requests ****************************************************************************************** */
// GET method to search an article
app.get("/searchArticle/:url", (request, response) => {
  let url = decodeURIComponent(request.params.url).slice(5);
  console.log("User searched: " + url);

  // Validate url here
  isValid = utils.validUrl(url);
  if (!isValid) {
    response.send("Invalid URL");
    return;
  }

  // Call to Python server for information here
  var reply = "Failed";
  var requester = zmq.socket("req");

  requester.connect("tcp://64.225.60.170:5555");
  requester.send("URL " + url);

  requester.on("message", function(reply) {
    reply = reply.toString();
    console.log("Received reply", ": [", reply, "]");
    requester.close();
    setTimeout(function() {
      response.send(reply);
    }, 1000);
  });
});

// GET method to recieve article information for an article
app.get("/getArticle", (request, response) => {
  console.log("User requested article information");

  res = "None";
  var requester = zmq.socket("req");
  requester.connect("tcp://64.225.60.170:5555");
  requester.send("Article");

  requester.on("message", function(res) {
    res = res.toString();
    console.log("getArticle success");
    requester.close();

    setTimeout(function() {
      response.send(res);
    }, 1000);
  });
});

// GET method to recieve author card information for an author
app.get("/getAuthorCard", (request, response) => {
  console.log("User requested author information");

  res = "None";

  var requester = zmq.socket("req");
  requester.connect("tcp://64.225.60.170:5555");
  requester.send("Author card");

  requester.on("message", function(res) {
    res = res.toString();
    console.log("getAuthorCard success");
    requester.close();

    setTimeout(function() {
      response.send(res);
    }, 1000);
  });
});

// GET method to recieve publisher card information for an article
app.get("/getPublisherCard", (request, response) => {
  console.log("User requested publisher information");

  res = "None";
  var requester = zmq.socket("req");
  requester.connect("tcp://64.225.60.170:5555");
  requester.send("Publisher card");

  requester.on("message", function(res) {
    res = res.toString();
    console.log("getPublisherCard success");
    requester.close();

    setTimeout(function() {
      response.send(res);
    }, 1000);
  });
});
