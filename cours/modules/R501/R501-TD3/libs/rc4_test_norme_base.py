# Test des valeurs de la norme 802.11 (2012) - Page 2619 Table M-5—ARC4 encryption
iv_key=bytes.fromhex('fb 02 9e 30 31 32 33 34')
plainText=bytes.fromhex(' \
aa aa 03 00 00 00 08 00 45 00 00 4e 66 1a 00 00 80 11 be 64 0a \
00 01 22 0a ff ff ff 00 89 00 89 00 3a 00 00 80 a6 01 10 00 01 \
00 00 00 00 00 00 20 45 43 45 4a 45 48 45 43 46 43 45 50 46 45 \
45 49 45 46 46 43 43 41 43 41 43 41 43 41 43 41 41 41 00 00 20 \
00 01 1b d0 b6 04')
cipherText=bytes.fromhex(' \
f6 9c 58 06 bd 6c e8 46 26 bc be fb 94 74 65 0a ad 1f 79 09 b0 \
f6 4d 5f 58 a5 03 a2 58 b7 ed 22 eb 0e a6 49 30 d3 a0 56 a5 57 \
42 fc ce 14 1d 48 5f 8a a8 36 de a1 8d f4 2c 53 80 80 5a d0 c6 \
1a 5d 6f 58 f4 10 40 b2 4b 7d 1a 69 38 56 ed 0d 43 98 e7 ae e3 \
bf 0e 2a 2c a8 f7')

iv_key_hex = iv_key.hex()
plainTextHex = plainText.hex()
cipherTextHex = cipherText.hex()

if __name__ == "__main__":
  print(f'IV+KEY: {iv_key.hex()}')
  print(f'Text  : {plainText.hex()}')
