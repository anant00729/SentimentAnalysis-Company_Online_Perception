if ('content_bert_main' in window) {
  content_bert_main()
}
else {
  const content_bert_main = () => { let headlines = []

  for(let _a of document.querySelectorAll('h3, h3 span,div[data-testid="tweetText"], h2 a, h2')){
    headlines.push(_a.textContent)
  }

  let requestBody = {
    sentences: headlines
  };

  const headers = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json'},
    body: JSON.stringify(requestBody)
  }

  console.log('requestBody', requestBody)

  fetch('http://127.0.0.1:5000/classify', headers)
  .then((res) => res.json())
  .then((data) => {
    const element = document.querySelectorAll('h3, h3 span,div[data-testid="tweetText"], h2 a, h2')
    for (let i = 0; i < data?.labels?.length; i++) {
      let ele = null;
      for (let j = 0; j < element.length; j++) {
        if (element[j]?.textContent === data?.labels[i]?.input) {
          ele = element[j];
        }
      }
      const isPositive = data?.labels[i]?.output === 'positive'
      if(ele){
        if (isPositive) {
          ele.style.color = 'green';
        }else {
          ele.style.color = 'red';
        }
      }
    }
  })
  .catch((error)=> {
    console.log('error', error)
  })
  }
  content_bert_main()
  // Observe for new headlines
  const observer = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      // bottom of the page has been reached
      console.log('bottom of page reached')
      // call your function to get new HTML tags
      content_bert_main()
    }
  })

  window.addEventListener('scroll', () => {
    const scrollPosition = window.innerHeight + window.scrollY
    const bodyHeight = document.body.offsetHeight
    if (scrollPosition >= bodyHeight) {
      // at the bottom of the page, observe the next element
      observer.observe(document.querySelector('footer'))
    }
  })
}

