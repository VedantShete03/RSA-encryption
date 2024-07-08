import socket
import rsa

# Generate RSA keys for the server
(server_pubkey, server_privkey) = rsa.newkeys(512)

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a public host, and a port
server.bind(('0.0.0.0', 8080))

# Become a server socket
server.listen(5)
print("Server listening on port 8080...")

while True:
    # Establish connection with Client 1
    client1_socket, addr = server.accept()
    print("Connected to Client 1")

    # Receive Client 1's public key
    client1_pubkey = rsa.PublicKey.load_pkcs1(client1_socket.recv(1024))

    # Send server's public key to Client 1
    client1_socket.send(server_pubkey.save_pkcs1())

    # Receive the encrypted message from Client 1
    encrypted_message = client1_socket.recv(1024)

    # Decrypt the message using server's private key
    decrypted_message = rsa.decrypt(encrypted_message, server_privkey)
    print("Decrypted message from Client 1:", decrypted_message.decode())

    # Close the connection with Client 1
    client1_socket.close()

    # Establish connection with Client 2
    client2_socket, addr = server.accept()
    print("Connected to Client 2")

    # Receive Client 2's public key
    client2_pubkey = rsa.PublicKey.load_pkcs1(client2_socket.recv(1024))

    # Encrypt the decrypted message with Client 2's public key
    reencrypted_message = rsa.encrypt(decrypted_message, client2_pubkey)

    # Send the re-encrypted message to Client 2
    client2_socket.send(reencrypted_message)

    # Close the connection with Client 2
    client2_socket.close()
