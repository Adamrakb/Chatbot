import aiml
import os

# Inisialisasi kernel AIML
kernel = aiml.Kernel()

# Load semua file AIML di folder data/
for file in os.listdir("data"):
    if file.endswith(".aiml"):
        kernel.learn(f"data/{file}")

print("Jarvis siap, silakan tanya apa saja!")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "keluar"]:
        print("Jarvis: Sampai jumpa, Abay!")
        break

    response = kernel.respond(user_input)

    if response:
        print("Jarvis:", response)
        os.system(f'espeak "{response}"')  # TTS output
    else:
        print("Jarvis: Maaf, aku belum mengerti.")
