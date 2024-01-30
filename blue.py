import bluetooth

def find_nearest_bluetooth_device():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    if nearby_devices:
        print(f"Trovati {len(nearby_devices)} dispositivi.")
        for addr, name in nearby_devices:
            print(f" {addr} - {name}")
        return nearby_devices[0][0]  # Restituisce l'indirizzo MAC del primo dispositivo trovato
    else:
        print("Nessun dispositivo trovato.")
        return None

def send_message(bd_addr):
    if bd_addr is None:
        print("Nessun indirizzo MAC fornito.")
        return
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))
    sock.send("Ciao, mondo!")
    sock.close()

bd_addr = find_nearest_bluetooth_device()
send_message(bd_addr)
