#!/bin/env python3
import os

try:
  import Crypto as pcr
except ModuleNotFoundError:
  os.system("pip install pycryptodome")

  import Crypto as pcr ### It should work now

from Crypto.Cipher import ARC4
from Crypto.Cipher.ARC4 import ARC4Cipher
from zlib import crc32
from libs.cb_utils import bytesXOR

from typing import Union
from termcolor import colored
from termcolor import COLORS

import libs.rc4_test_norme_base as base


def cipherData(text2Cipher: str | bytes, key: bytes, returnKey: bool = False) -> Union[str | bytes] | dict[str: ARC4Cipher | Union[str | bytes]]:
  working_key = None
  working_text = None

  ### Type assertion and verification
  if type(text2Cipher) == str:
    working_text = bytes.fromhex(text2Cipher)
  else:
    working_text = text2Cipher

  if type(key) == str:
    working_key = bytes.fromhex(key)
  else:
    working_key = key

  cipher = ARC4.new(working_key)
  cipheredText = cipher.encrypt(working_text)

  if not returnKey:
    return cipheredText

  return {
    "cipher": cipher,
    "text": cipheredText
  }

def decipherData(textCiphered: str | bytes, key: ARC4.ARC4Cipher, iv_key: bytes) -> str | bytes:
  working_key = None
  working_text = None

  ### Type assertion and verification
  if type(textCiphered) == str:
    working_text = bytes.fromhex(textCiphered)
  else:
    working_text = textCiphered

  if type(iv_key) == str:
    working_key = bytes.fromhex(iv_key)
  else:
    working_key = iv_key

  decipheredText = key.decrypt(working_text)

  new_key = ARC4.new(working_key)
  decipheredTextWithNewKey = new_key.decrypt(working_text)

  return decipheredText, decipheredTextWithNewKey

def newDecipherData(textCiphered: str | bytes, key: str | bytes):
  working_key = None
  working_text = None

  ### Type assertion and verification
  if type(textCiphered) == str:
    working_text = bytes.fromhex(textCiphered)
  else:
    working_text = textCiphered

  if type(key) == str:
    working_key = bytes.fromhex(key)
  else:
    working_key = key

  ### Now we can work with the bytes

  cipher = ARC4.new(working_key)
  decryptedData = cipher.decrypt(working_text)

  return decryptedData

def determineKeyFromDataStreams(dataStream: list[str]):
  ...

def printQuestion(QuestionNumber: str, title: str) -> None:
  print("\n/////////////////////////////////////////////////////////////////////////////////")
  print(f"////              {QuestionNumber} - {title}")
  print("/////////////////////////////////////////////////////////////////////////////////", end="\n\n")

def printNotFinished():
  casing = colored("/////////////////////////////////////////////////////////////////////////////////", "light_red")

  print(f"\n{casing}")
  print(colored("//// TODO: THIS IS NOT FINISHED", "light_red"))
  print(f"{casing}", end="\n\n")

if __name__ == "__main__":
  print(f"Base:\n- Cipher text: {base.cipherTextHex}\n- Plain text: {base.plainTextHex}\n- IV Key: {base.iv_key_hex}")

  printQuestion("1.2", "ARC4 Chiffrement de données")

  cipheredData = cipherData(base.plainText, base.iv_key)
  print("Newly ARC4 Ciphered data:", cipheredData.hex())
  print("Well encrypted" if cipheredData.hex() == base.cipherTextHex else "Not well encrypted", "!")


  printQuestion("1.3", "Déchiffrement trame WEP")
  cipheredDataWithKey = cipherData(base.plainText, base.iv_key, True)
  decipheredData = decipherData(cipheredDataWithKey["text"], cipheredDataWithKey["cipher"], base.iv_key)

  print("Decrypted data with same key/cipher:", decipheredData[0].hex())
  print("Decrypted data with reinitialized key:", decipheredData[1].hex())

  print("Well decrypted with old key" if decipheredData[0].hex() == base.plainTextHex else "Not well decrypted with old key")
  print("Well decrypted with reinitialized key" if decipheredData[1].hex() == base.plainTextHex else "Not well decrypted with reinitialized key")

  printQuestion("1.4", "Déchiffrement trame WEP40 Wireshark")

  trameWEP40Data = "01fcdcf7429af0211694c59d15e5397fd127d4dc3d7c92a8f2ba5495dadd3f6994ece50ebd45d9a372656c02777808196270c02cbe54"
  trameWEP40Key = bytes.fromhex("753054" + "1111111111")
  decipheredTrame = newDecipherData(trameWEP40Data, trameWEP40Key)

  print("Trame chiffrée:", trameWEP40Key.hex())
  print("Trame déchiffrée:", decipheredTrame.hex())
  print("Bon déchiffrement !" if "aaaa03" in decipheredTrame.hex() else "Mauvais déchiffrement !")

  printQuestion("1.5", "Validation de données avec ICV")

  icv = crc32(decipheredTrame)
  icvHex = hex(icv)

  print(f"ICV: {icvHex}")

  ### TODO: NOT DONE
  printNotFinished()

  printQuestion("1.6", "Equivalence de chiffrement")

  #### KS = KeyStream
  #### MSG = CipherTrame
  #### KS + DecryptedTrame =

  msg = bytes.fromhex(trameWEP40Data)
  ks_pdu = "0"*len(trameWEP40Data)
  ks_pdu = bytes.fromhex(ks_pdu)

  ks = cipherData(ks_pdu, trameWEP40Key)
  xor_encryption = bytesXOR(ks, msg)

  print("KS PDU:", ks_pdu.hex())
  print("KS:", ks.hex())
  print("Ciphered:", msg.hex())
  print("Result:", xor_encryption.hex())

  printQuestion("1.7", "Déchiffrement de C avec KS")

  printNotFinished()

  ### TODO: NOT DONE

  printQuestion("2.1", "Déterminer la valeur des 6 octets d'entête des trames 1, 2 et 4")



  trame1 = bytes.fromhex("010001000000")
  trame2 = bytes.fromhex("010002000000")
  trame4 = bytes.fromhex("010004000000")

  print(f"La trame 1 a comme 6 octets d'entête: {trame1.hex(' ')}")
  print(f"La trame 2 a comme 6 octets d'entête: {trame2.hex(' ')}")
  print(f"La trame 4 a comme 6 octets d'entête: {trame4.hex(' ')}")

  printNotFinished()

  printQuestion("2.2", "Déduire les 6 octets d'entête de la trame 3")

  print("La trame 3 aura les 6 octets suivants `01 00 03 00 00 00`")
