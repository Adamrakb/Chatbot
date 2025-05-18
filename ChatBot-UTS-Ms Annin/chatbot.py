import aiml
import os
import speech_recognition as sr
import pyttsx3

# Inisialisasi AIML Kernel
kernel = aiml.Kernel()

# Load semua file AIML dari folder data/
for file in os.listdir("data"):
    if file.endswith(".aiml"):
        kernel.learn(f"data/{file}")

# Inisialisasi TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', engine.getProperty('voices')[0].id)  # Gunakan suara default

# Inisialisasi Speech Recognition
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with microphone as source:
        print("(Mendengarkan...)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio, language="id-ID")
    except sr.UnknownValueError:
        print("(Tidak bisa mengenali suara)")
        return input("You (ketik): ")
    except sr.RequestError:
        print("(Gagal menghubungi layanan pengenalan suara)")
        return input("You (ketik): ")

print("Jarvis siap, silakan bicara atau ketik pertanyaan!")

while True:
    user_input = listen()
    if user_input.lower() in ["exit", "quit", "keluar"]:
        speak("Sampai jumpa, Abay!")
        break

    response = kernel.respond(user_input)

    if response:
        speak(response)
    else:
        speak("Maaf, aku belum mengerti.")
