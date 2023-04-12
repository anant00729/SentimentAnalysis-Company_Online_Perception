// background.js

console.log("Background script running!");

chrome.runtime.onInstalled.addListener(() => {
  console.log("Extension installed.");
});

chrome.runtime.onStartup.addListener(() => {
  console.log("Extension started up.");
});
