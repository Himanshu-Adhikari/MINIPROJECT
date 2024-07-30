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

<img src="https://github.com/user-attachments/assets/5468631c-551c-4072-9be7-7151bdd1dd40" alt="Landing Page" width="300"/>

### Results Page
Page displaying the sentiment analysis result and feedback.

<img src="https://github.com/user-attachments/assets/54fe7e77-b0cb-424f-846e-6b3e7075ce3a" alt="ResultPage" width="300"/>
<img src="https://github.com/user-attachments/assets/3512e770-a686-487e-8c35-b92ebc6752ed" alt="Results" width="300"/>

## How It Works

1. **Choose Input Method**: Users can either type in text or use the audio input feature.
2. **Perform Sentiment Analysis**: The text (converted from speech or directly input) is analyzed using a BERT model.
3. **Translate if Needed**: If the input is in a language not directly supported by the BERT model, the Google Translation API translates it to a supported language.
4. **Get Feedback**: The analyzed sentiment is fed to Gemini for feedback.
<img src="https://github.com/user-attachments/assets/faf8e29d-85d1-4289-a0e6-8b10a2a5a89a" alt="Image" width="300"/>
