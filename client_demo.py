import socket
import json

class HardwareConfigClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def request_hardware_config(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))

            data = client_socket.recv(4096)
            hardware_config = json.loads(data.decode("utf-8"))

            return hardware_config

if __name__ == "__main__":
    client = HardwareConfigClient("127.0.0.1", 8080)
    hardware_config = client.request_hardware_config()

    print("\nReceived Hardware Configuration:")
    for key, value in hardware_config.items():
        print(f"\n{key}:")
        for sub_key, sub_value in value.items():
            print(f"{sub_key}: {sub_value}")
