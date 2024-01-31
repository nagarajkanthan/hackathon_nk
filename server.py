import socket
import json

class HardwareConfigServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.hardware_config = self.load_hardware_config()

    def load_hardware_config(self, filename="hardware_config.json"):
        with open(filename, "r") as json_file:
            return json.load(json_file)

    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen()

            print(f"Server listening on {self.host}:{self.port}...")

            while True:
                client_socket, client_address = server_socket.accept()
                print(f"Connection from {client_address}")

                with client_socket:
                    data = json.dumps(self.hardware_config).encode("utf-8")
                    client_socket.sendall(data)
                    print("Data sent to the client.")

if __name__ == "__main__":
    server = HardwareConfigServer("127.0.0.1", 8080)
    server.start_server()
