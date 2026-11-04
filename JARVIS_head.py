# importiamo libreria "requests" che ci serve per chiamare le API
import requests
import speech_recognition as sr  # <-- DEVE ESSERCI

def trova_meteo(citta, api_key):
    # Usiamo "units=metric" per i gradi Celsius e "lang=it" per la descrizione in italiano
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    parametri = {
        'q' : citta,
        'appid' : api_key,
        'units' : 'metric', # selezioniamo i celsius
        'lang' : 'it', # lingua italiana
    }

    try:
        # request.get manda l'ordine
        risposta = requests.get(base_url, params=parametri)
        # l'api risponde con un json che python trasforma in un dizionario
        dati = risposta.json()
        # 200 = ok
        if risposta.status_code == 200:
            descrizione = dati["weather"][0]["description"]
            temperatura = dati["main"]["temp"]
            # risposta
            output_jarvis = f"Certo. A {citta} ci sono {temperatura}°C e il tempo è {descrizione}."
            return output_jarvis
        else:
            # errore dato dal server
            print(f"DEBUG: Il server ha risposto con codice: {risposta.status_code}")
            # stampare messaggio di errore
            print(f"DEBUG: Messaggio dell'API: {dati}")
            return f"Mi dispiace, non sono riuscito a trovare il meteo per {citta}"
    except Exception as e:
        return f"C'è stato un errore di connessione: {e}"

def ascolta_comando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("JARVIS in ascolto...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        testo = r.recognized_google(audio, language="it-IT")
        print(f"UTENTE: {testo}")
        return testo
    except sr.UnknownValueError:
        return "Non ho capito."
    except sr.RequestError as e:
        return f"Errore del servizio di riconoscimento vocale; {e}"

if __name__ == "__main__":
    CHIAVE_API = "INSERISCI LA TUA CHIAVE API"

    comando_vocale = ascolta_comando()
    if comando_vocale != "Non ho capito." and "Errore" not in comando_vocale:
        citta_input = comando_vocale
        risposta_finale = trova_meteo(citta_input, CHIAVE_API)
        print(f"JARVIS: {risposta_finale}")
    else:
        print(f"JARVIS: {comando_vocale}")

    #citta_input = input("Per quale città vuoi conoscere il meteo? ")
    #risposta_finale = trova_meteo(citta_input, CHIAVE_API)
    #print(f"JARVIS: {risposta_finale}")