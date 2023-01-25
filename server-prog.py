import random
import socket
import threading

quotes = [
    "The internet is the new battleground of earth, the wild west, the place of truth and opportunity.",
    "Life is a game of chess, chess is life.",
    "Depression is motivation’s toxic waste.",
    "The most important skill you need as a man is the ability to manipulate opponents and pick your battles.",
    "If failure makes you stronger, you can never lose.",
    "You’ve never pushed yourself because you believe the goal can never be achieved.",
    "The harder you work, the more important you become.",
    "The minimum requirements to be a winner are achievable.",
    "If you love yourself, you will build yourself.",
    "When you’ve broken a record, that record is now a new standard."
]

def handle_client(client_socket):
    quote = random.choice(quotes)
    client_socket.send(quote.encode())
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.3.131", 8888))
server.listen(5)

print("Quote of the Day server is listening on port 8888...")

while True:
    client, addr = server.accept()
    print("Received connection from: ", addr)
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
