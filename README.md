# Multilingual Sentimental Analysis React App

This project is designed to perform sentiment analysis on user input, supporting multiple languages. The app can take input via audio (converted to text using the `react-speech-kit` library) or directly as text, which is then analyzed by a BERT sentiment analysis model. The app extends the original model's language support using the Google Translation API and provides feedback based on the analysis using Gemini.

## Features

- **Multilingual Support**: Analyzes text in multiple languages using the Google Translation API.
- **Audio Input**: Converts speech to text using the `react-speech-kit` library.
- **Text Input**: Direct text input for sentiment analysis.
- **BERT Sentiment Analysis**: Uses a BERT model to determine sentiment.
- **Feedback System**: Provides feedback based on the sentiment using Gemini.

## Tech Stack

- **Frontend**: React, Tailwind CSS, react-speech-kit
- **Backend**: Python, Flask
- **API**: Google Translation API, Gemini

## Screenshots

### Landing Page
The landing page where users can choose to input text or use audio for sentiment analysis.

![Landing Page](URL_TO_LANDING_PAGE_IMAGE)

### Input Page
Page where users input text or use the audio feature.

![Input Page](URL_TO_INPUT_PAGE_IMAGE)

### Results Page
Page displaying the sentiment analysis result and feedback.
![WhatsApp Image 2024-07-10 at 11 12 32_64a72488](https://github.com/user-attachments/assets/7a634db3-804b-4ad7-babf-a8ba72e074a6)

![Results Page](![WhatsApp Image 2024-07-10 at 11 12 32_64a72488](https://github.com/user-attachments/assets/7a634db3-804b-4ad7-babf-a8ba72e074a6)
)

## How It Works

1. **Choose Input Method**: Users can either type in text or use the audio input feature.
2. **Perform Sentiment Analysis**: The text (converted from speech or directly input) is analyzed using a BERT model.
3. **Translate if Needed**: If the input is in a language not directly supported by the BERT model, the Google Translation API translates it to a supported language.
4. **Get Feedback**: The analyzed sentiment is fed to Gemini for feedback.

## Getting Started

To run this project locally, follow these steps:

### Clone the repository
```sh
git clone https://github.com/your-repo/multilingual-sentimental-analysis.git
cd multilingual-sentimental-analysis
