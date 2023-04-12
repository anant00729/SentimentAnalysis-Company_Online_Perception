# BERT-based Sentiment Analysis: A Chrome Extension for Analyzing Text Sentiment.

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Chrome Extension](https://img.shields.io/badge/Google_chrome-4285F4?style=for-the-badge&logo=Google-chrome&logoColor=white)

## 🪟 Overview
We have developed a Chrome extension that utilizes BERT to analyze the sentiment of headlines from New York Times and Wall Street Journal. By filtering out negative articles, it has the potential to personalize news feeds and create a more efficient news consumption experience. The BERT model processes each article's headline in real-time, predicting whether the article has a positive or negative sentiment. This functionality can enhance user experience, save time, and increase awareness of the overall news sentiment.

***
## ⌨️ Getting started

**1. Running the flask backend server:**


- Ensure that all the required Python packages are included in the requirements.txt file.

```
pip install -r requirements.txt
```

- The Flask application utilizes the `bert-base-uncased_4000_0_best.pt` model file. Please ensure that you run the `download_models.py` file to download the model from Google Drive.

- You can start the server by running the following command:

```
python app.py
```

- The following URL will be used to run the server

```
http://127.0.0.1:5000/
```

**2. Installing Chrome Extension to the browser:**

- Launch the Chrome browser and go to 

```
chrome://extensions/
```

- Select the "Load unpacked" button located at the top left corner.

<img width="926" alt="Screen Shot 2023-04-07 at 4 45 06 PM" src="https://user-images.githubusercontent.com/20675885/230692923-2a107705-7985-4079-8d96-9baa6a482b46.png">

- Choose the folder named `chrome-ext-client` which contains the unpacked files of the Chrome extension and has a file called `manifest.json`.

<img width="1435" alt="Screen Shot 2023-04-07 at 4 52 34 PM" src="https://user-images.githubusercontent.com/20675885/230693868-109cc0ac-c57d-4b11-97e1-2dcc9352e44e.png">


- Open the extension menu

<img width="416" alt="Screen Shot 2023-04-07 at 4 49 16 PM" src="https://user-images.githubusercontent.com/20675885/230693608-ee6f8159-3ac1-49e6-a809-23fb93d07446.png">

- Pin the extension

<img width="361" alt="Screen Shot 2023-04-07 at 4 56 47 PM" src="https://user-images.githubusercontent.com/20675885/230693942-2cb54ed4-7208-4880-b24d-35b9b16f150b.png">

- Access the extension and navigate to any of the following websites. 
1. https://www.nytimes.com/
2. https://www.wsj.com/
 
- To get the sentiments, click on the extension icon and then click on the "Get Sentiments" button inside the extension popup.

<img width="1440" alt="Screen Shot 2023-04-07 at 4 58 23 PM" src="https://user-images.githubusercontent.com/20675885/230694022-152cf0ca-cd54-440f-ac35-eaf915633d60.png">


***

## 🎬 Results

Titles displayed in green indicate a positive sentiment, while those in red indicate a negative sentiment.

1. https://www.nytimes.com/

<img width="1261" alt="Screen Shot 2023-04-07 at 5 03 50 PM" src="https://user-images.githubusercontent.com/20675885/230694291-1ffa4e20-e4f2-487c-8e37-a5a5da21f2cd.png">

<img width="1274" alt="Screen Shot 2023-04-07 at 4 30 34 PM" src="https://user-images.githubusercontent.com/20675885/230694104-88135c6c-5f63-4ce4-b536-8dca2840c969.png">


2. https://www.wsj.com/

<img width="1089" alt="Screen Shot 2023-04-07 at 5 07 18 PM" src="https://user-images.githubusercontent.com/20675885/230694462-34393193-726f-4c92-b643-e595aeda9ef4.png">

<img width="1070" alt="Screen Shot 2023-04-07 at 5 07 49 PM" src="https://user-images.githubusercontent.com/20675885/230694463-2836962d-cfad-482d-a272-0deb212d908b.png">

