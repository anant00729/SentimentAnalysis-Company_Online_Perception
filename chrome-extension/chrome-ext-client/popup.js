// document.addEventListener('DOMContentLoaded', function() {
//   let getHtmlBtn = document.getElementById('getHtmlBtn');
//   getHtmlBtn.addEventListener('click', function() {
//     chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
//       let tab = tabs[0];
//       chrome.scripting.executeScript({
//         target: { tabId: tab.id },
//         function: getPageHtml,
//       }, (results) => handleGetPageTitleResponse(results, tab.id));
//     });
//   });
// });

// const handleGetPageTitleResponse = async (results, id) => {
//   let output = document.getElementById('output');
//   let html = results[0].result;
//   let requestBody = {
//     sentences: html
//   };
//   alert(JSON.stringify(requestBody))
//   try {
//     // Use the fetch function to send a POST request to the API endpoint
//     const response = await fetch('http://127.0.0.1:5000/classify', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json'
//       },
//       body: JSON.stringify(requestBody)
//     });

//     // Parse the JSON response and log the data to the console
//     const data = await response.json();
//     handleAPIResponse(data);
//   } catch (error) {
//     // Log any errors to the console
//     output.textContent = error.toString();
//   }
// };



// const handleAPIResponse = (data) => {
//   chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
//     let tab = tabs[0];
//     // alert(tab.id);
//     chrome.scripting.executeScript({
//       target: { tabId: tab.id },
//       function: function(data) {
//         const elements = document.querySelectorAll('h3, h3 span,div[data-testid="tweetText"]');
//         for (let i = 0; i < data?.labels?.length; i++) {
//           let ele = null;
//           for (let j = 0; j < elements.length; j++) {
//             if (elements[j]?.textContent === data?.labels[i]?.input) {
//               ele = elements[j];
//             }
//           }
//           const isPositive = data?.labels[i]?.output === 'positive' 
//           if(ele){
//             if (isPositive) {
//               ele.style.color = 'green';
//             }else {
//               ele.style.color = 'red';
//             }
//           }
//         }
//       },
//       args: [data],
//     });
//   });
// };

// const getPageHtml = () => {
//   let element = document.querySelectorAll('h3, h3 span,div[data-testid="tweetText"]');
//   let headlines = []
//   for(let _a of element){
//     headlines.push(_a.textContent)
//   }
//   if (element) {
//     return headlines;
//   } else {
//     return 'Headline not found.';
//   }
// };


document.getElementById("activate-script").addEventListener("click", async () => {


  // const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  // const result = await chrome.scripting.executeScript({
  //   target: { tabId: tab.id },
  //   func: () => {
  //     console.log('__DARA ', JSON.stringify(Array.from(document.getElementsByTagName('script')).map(d => d.src)))
  //     return Array.from(document.getElementsByTagName('script'))
  //     .some(script => script.src.includes('content_bert.js'));
  //   }
  // });
  // const isActive = result[0].result;

  // alert(isActive)

  // console.log('isActive', isActive)
  
  // alert(`Content script is ${isActive ? 'active' : 'not active'}`);



  chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
    alert(tabs[0].id)
    chrome.scripting.executeScript({
      target: {tabId: tabs[0].id},
      files: ["content_bert.js"]
    });
  });

  // chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
  //   chrome.scripting.executeScript({
  //     target: {tabId: tabs[0].id},
  //     function: () => {
  //       const scriptEls = document.querySelectorAll('script');
  //     const isContentJsLoaded = Array.from(scriptEls).find(el => el.src.endsWith('hook.js'));
  //       if (scriptEl) {
  //         scriptEl.remove();
  //       }
  //     }
  //   });
  // });


  // chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
  //   alert(tabs[0].id)
  //   chrome.scripting.executeScript({
  //     target: {tabId: tabs[0].id},
  //     function: () => {
  //       const scriptEls = document.querySelectorAll('script');
  //       const isContentJsLoaded = Array.from(scriptEls).some(el => el.src.endsWith('hook.js'));
  //       console.log(isContentJsLoaded);
  //     }
  //   });
  // });
});


