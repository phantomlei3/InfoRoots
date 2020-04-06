import axios from "axios";

// Request for processing a user's search query
export async function processUserSearch(searchQuery) {
  console.log("Searched: '" + searchQuery + "'");
  let searchQueryRes = await axios.get(
    "/searchArticle/" + "&url=" + encodeURIComponent(searchQuery)
  );
  return searchQueryRes;
}

// Request for recieving article information
export async function getArticle(url) {
  console.log("Getting Article Information: " + url);
  let res = await axios.get("/getArticle");
  return res;
}

// Request for recieving author Information
export async function getAuthor(url) {
  console.log("Getting Author Information: " + url);
  let res = await axios.get("/getAuthorCard");
  return res;
}
