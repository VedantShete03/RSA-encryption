import socket
import rsa

# Generate RSA keys for Client 1
(client1_pubkey, client1_privkey) = rsa.newkeys(512)

# Create a socket object
client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client1.connect(('127.0.0.1', 8080))

# Send Client 1's public key to the server
client1.send(client1_pubkey.save_pkcs1())

# Receive the server's public key
server_pubkey = rsa.PublicKey.load_pkcs1(client1.recv(1024))

# Message to be encrypted
message = "Hello from Client 1"

# Encrypt the message using the server's public key
encrypted_message = rsa.encrypt(message.encode(), server_pubkey)

# Send the encrypted message to the server
client1.send(encrypted_message)

# Close the connection
client1.close()
