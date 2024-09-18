#!/bin/env python3

import os
try:
  from termcolor import colored
except ModuleNotFoundError:
  os.system("pip install termcolor")

########################################################################
########################################################################
# Decoupe la chaine en paquets de 2 digits
# '112233AABBCC' => ['11','22','33','AA','BB','CC']
def cbSplitHex(hexStr,size=2):
  return [hexStr[i:i+size] for i in range(0,len(hexStr),size)]

def strCheckOK(ok,m1='ok',m2='BAD !!!'):
  txt=colored(m1,'green')
  if not ok:
    txt=colored(m2,'red')
  return txt

# XOR entre 2 bytes
def bytesXOR(a,b):
  assert len(a)==len(b)
  x=int.from_bytes(a,byteorder='big')^int.from_bytes(b,byteorder='big')
  return x.to_bytes(len(a),byteorder='big')

if __name__=='__main__':
  m=bytes.fromhex('abcdef')
  ks=bytes.fromhex('123456')
  c=bytesXOR(m,ks)
  d=bytesXOR(c,ks)
  print(f'{m.hex()} xor {ks.hex()} = {c.hex()} {strCheckOK(c.hex()=="b9f9b9")}')
  print(f'{c.hex()} xor {ks.hex()} = {d.hex()} {strCheckOK(d==m)}')
