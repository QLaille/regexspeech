import speech_recognition as sr

def get_speech() :
	r = sr.Recognizer()

	sr.Microphone.list_microphone_names()

	mic = sr.Microphone()

	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)

	try:
		response = r.recognize_google(audio)
	except sr.RequestError:
		response = ""
	except sr.UnknownValueError:
		response = ""
