import socket
import threading
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

users = {}          # phone_number -> socket
call_history = []   # list of dicts

print("📡 Server running...")

def handle_client(client):
    phone = client.recv(1024).decode()
    users[phone] = client
    print(f"✅ {phone} connected")

    try:
        while True:
            data = client.recv(1024).decode()
            if not data:
                break

            parts = data.split("|")

            if parts[0] == "CALL":
                caller, receiver = parts[1], parts[2]
                if receiver in users:
                    users[receiver].send(f"INCOMING|{caller}".encode())
                    call_history.append({
                        "from": caller,
                        "to": receiver,
                        "time": datetime.now().strftime("%H:%M"),
                        "type": "outgoing"
                    })
                else:
                    client.send("USER_OFFLINE".encode())

    except:
        pass
    finally:
        print(f"❌ {phone} disconnected")
        users.pop(phone, None)
        client.close()

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_client, args=(client,), daemon=True).start()
