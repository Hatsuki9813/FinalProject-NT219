import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def logistic_map_key(length):
    x = 0.5
    key = []
    for _ in range(length):
       x = 3.99 * x * (1 - x)
       key.append(int(x * 256) % 256)
    return bytes(key)
def decrypt_video(input_file, output_file, key, nonce):
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        while chunk := f_in.read(64 * 1024):
            decrypted_chunk = decryptor.update(chunk)
            f_out.write(decrypted_chunk)
        f_out.write(decryptor.finalize())
