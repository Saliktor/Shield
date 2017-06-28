import hashlib

h = hashlib.new('sha256')
h.update("thi".encode('utf-8'))
print(h.hexdigest())

def encrypt(key, msg):
    encrypted = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encrypted.append(chr((msg_c + key_c) % 127))
    return ''.join(encrypted)

def decrypt(key, encryption):
    msg = []
    for i, c in enumerate(encryption):
        key_c = ord(key[i%len(key)])
        encrypt_c = ord(c)
        msg.append(chr((encrypt_c - key_c) % 127))
    return ''.join(msg)