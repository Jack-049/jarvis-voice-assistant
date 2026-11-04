import pyaudio

p = pyaudio.PyAudio()

print("\n--- Ricerca Dispositivi Audio ---")

info = p.get_host_api_info_by_index(0)
num_devices = info.get('deviceCount')

print(f"Trovati {num_devices} dispositivi in totale.\n")

print("--- Elenco Dispositivi di INPUT (Microfoni) ---")
for i in range(0, num_devices):
    device_info = p.get_device_info_by_host_api_device_index(0, i)
    # Controlla solo i dispositivi di INPUT (maxInputChannels > 0)
    if (device_info.get('maxInputChannels')) > 0:
        print(f"Dispositivo index {i}: {device_info.get('name')}")

print("----------------------------------------------")
p.terminate()