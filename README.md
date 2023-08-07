## Artificial Intelligence Voice Chat

#### Features 🌟
Transcription: Transcribes audio using OpenAI's Whisper 🎙️

Text-to-Speech: Using the power of pyttsx3, text is converted to speech 🗣️

By default this uses the GPT-3.5 Turbo model but can be easily updated

#### Getting Started 🚀
Ensure you have the required Python packages installed. If not, you can easily install them using the requirements.txt file included in this repository. Simply run:

``` bash
pip install -r requirements.txt
```

Get your OpenAI API key from: https://platform.openai.com/account/api-keys
Copy it into a new .env file.

Here's a simple command to do that:

On macOS/Linux:

``` bash
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
```

On Windows:

``` bash
echo OPENAI_API_KEY=your_openai_api_key_here >> .env
```

To start a conversation, all you need to do is run the Python script provided. Feel welcome to submit Pull Requests.

#### How to Use 🗨️

Voice Interaction
Run the script, and make sure your microphone is set up correctly. Then, speak.

#### Tips for a Great Experience 🎉
1. Keep your audio clear and concise.
2. Play with the `no_speech_prop` comparison amount to adjust the sensitivity of the speech recognition & requests to  OpenAI's API's.
3. You can run the voices.py script to see what voices are available to you. You can then change the voice id in the main.py script.
4. The drivers for the pyttsx3 library vary from system to system. It's `nsss` for macOS, and `sapi5` for Windows. You can change this in the main.py script.

Have Fun! 🎈

Cheers,

Erik Bahena





