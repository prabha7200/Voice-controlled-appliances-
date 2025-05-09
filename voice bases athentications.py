import speech_recognition as sr

# The passphrase to authenticate
PASS_PHRASE = "my voice is my password"

# Initialize recognizer
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say your authentication phrase...")
    audio = recognizer.listen(source)

    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio).lower()
        print(f"You said: {text}")

        # Check against passphrase
        if text == PASS_PHRASE:
            print("Access Granted.")
        else:
            print("Access Denied.")

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Speech Recognition error; {e}")
