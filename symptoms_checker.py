import random
import speech_recognition as sr

# Sample symptom-to-disease mapping
disease_data = {
    "fever": ["Flu", "Malaria", "COVID-19"],
    "cough": ["Cold", "Bronchitis", "COVID-19"],
    "headache": ["Migraine", "Tension Headache", "Dehydration"],
    "stomach pain": ["Food Poisoning", "Gastritis", "Ulcer"],
    "fatigue": ["Anemia", "Diabetes", "Chronic Fatigue Syndrome"]
}

def predict_disease(symptoms):
    possible_diseases = []
    for symptom in symptoms:
        if symptom in disease_data:
            possible_diseases.extend(disease_data[symptom])
    
    if possible_diseases:
        return list(set(possible_diseases))  # Remove duplicates
    else:
        return ["No clear diagnosis. Please consult a doctor."]

def get_symptoms_by_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for symptoms... Speak now:")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            symptoms = recognizer.recognize_google(audio).lower()
            return symptoms.split()  # Convert speech to list of words
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand. Please try again.")
            return []
        except sr.RequestError:
            print("Error with speech recognition service. Check your internet.")
            return []

def main():
    print("ðŸ‘¨â€âš• Welcome to AI Doctor Chatbot! Type or Speak Your Symptoms.")
    print("Sorry the speech recognition is down right now!!!")
    choice = input("Press 'T' to type symptoms or 'S' for speech input: ").strip().lower()
    
    
    if choice == "s":
        symptoms = get_symptoms_by_voice()
    else:
        symptoms = input("Enter your symptoms separated by commas: ").lower().split(", ")

    if symptoms:
        diseases = predict_disease(symptoms)
        print("\nðŸ” Possible Diagnoses:")
        for disease in diseases:
            print(f"âœ… {disease}")
    else:
        print("No symptoms detected. Please try again.")

if __name__ == "__main__":
    main()
