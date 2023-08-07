import pyttsx3

# List available voices
engine = pyttsx3.init(driverName='nsss')
voices = engine.getProperty('voices')
for voice in voices:
    if voice.gender == "VoiceGenderFemale" and voice.languages[0] == "en_US":
        print("Voice ID:", voice.id)
        print("Name:", voice.name)
        print("Languages:", voice.languages)
        print("Gender:", voice.gender)
        print("Age:", voice.age)
        print("\n")
# tessa, samantha, alex, 
# Set the desired voice ID
desired_voice_id = "com.apple.speech.synthesis.voice.tessa"  # Replace with the desired voice ID

# Initialize the engine with the desired voice
engine.setProperty('voice', desired_voice_id)

# The text to be spoken
text = "Hello, this is a test message."

# Speak the text
engine.say('Hello! How are you?')
engine.runAndWait()