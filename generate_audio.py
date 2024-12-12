from gtts import gTTS
import os

# Create audio directory if it doesn't exist
if not os.path.exists('audio'):
    os.makedirs('audio')

# Dictionary of words and their approximate pronunciations
words = {
    'neih-hou': 'nay how',
    'do-jeh': 'doh jay',
    'joi-gin': 'joy gin',
    'jou-san': 'joe san'
}

# Generate audio files
for filename, text in words.items():
    print(f"Generating {filename}.mp3...")
    tts = gTTS(text)
    tts.save(f'audio/{filename}.mp3')

print("Audio files generated successfully!") 