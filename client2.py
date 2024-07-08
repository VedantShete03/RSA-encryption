import socket
import rsa

# Generate RSA keys for Client 2
(client2_pubkey, client2_privkey) = rsa.newkeys(512)

# Create a socket object
client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client2.connect(('127.0.0.1', 8080))

# Send Client 2's public key to the server
client2.send(client2_pubkey.save_pkcs1())

# Receive the encrypted message from the server
reencrypted_message = client2.recv(1024)

# Decrypt the message using Client 2's private key
decrypted_message = rsa.decrypt(reencrypted_message, client2_privkey)
print("Decrypted message from Client 1:", decrypted_message.decode())

# Close the connection
client2.close()
