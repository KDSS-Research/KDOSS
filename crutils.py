#################################################
#                                               #
#  Crutils library written by KoffiDev in 2020  #
#  Used: A1Z26 github, hashlib                  #
#                                               #
#################################################
import hashlib
import base64
import os
from arc4 import ARC4
from Crypto.Hash import MD2
__support__alg__ = ("base64", "base32", "base16", "base85", "A1Z26",
                    "md5", "sha1", "sha224", "sha256", "sha384", "sha512",
                    "arcfour")     
def b64encrypt(__arg__):
    __enc__bytes__ = __arg__.encode('ascii')
    __b64byt__ = base64.b64encode(__enc__bytes__)
    __result__ = base64_bytes.decode('ascii')
    return __result__
def b64decrypt(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message
def b16encrypt(messageh):
    message_bytes1 = messageh.encode('ascii')
    base16_bytes = base64.b16encode(message_bytes1)
    base16_message = base16_bytes.decode('ascii')
    return base16_message
def b16decrypt(base64_message):
    base16_bytes = base64_message.encode('ascii')
    message_bytes1 = base64.b16decode(base16_bytes)
    message1 = message_bytes1.decode('ascii')
    return message1
def b32encrypt(messageh):
    message_bytes1 = messageh.encode('ascii')
    base32_bytes = base64.b32encode(message_bytes1)
    base32_message = base32_bytes.decode('ascii')
    return base32_message
def b32decrypt(base32_message):
    base32_bytes = base32_message.encode('ascii')
    message_bytes1 = base64.b32decode(base32_bytes)
    message1 = message_bytes1.decode('ascii')
    return message1
def b85encrypt(messageh):
    message_bytes1 = messageh.encode('ascii')
    base32_bytes = base64.b32encode(message_bytes1)
    base32_message = base32_bytes.decode('ascii')
    return base32_message
def b85decrypt(base32_message):
    base32_bytes = base32_message.encode('ascii')
    message_bytes1 = base64.b32decode(base32_bytes)
    message1 = message_bytes1.decode('ascii')
    return message1
def A1Z26encrypt(cistring):
	string = ""	
	cistring = cistring.lower()	
	cistring = "".join(cistring.split())
	for x in range(0, len(cistring)):
		char = ord(cistring[x]) - 96
		if char > 0 and char <= 26 : string += str(char) + " "
	return(string)
def A1Z26decrypt(cistring):
	string = ""
	data = cistring.split()
	
	for char in data:
		char = chr(int(char) + 96)
		string += char
	return(string)
def md5encrypt(string1):
    md5_object = hashlib.md5(string1.encode())
    return md5_object.hexdigest()
def sha1encrypt(string):
    sha1_object = hashlib.sha1(string.encode())
    return sha1_object.hexdigest()
def sha224encrypt(string):
    sha224_object = hashlib.sha224(string.encode())
    return sha224_object.hexdigest()
def sha256encrypt(string):
    sha256_object = hashlib.sha256(string.encode())
    return sha256_object.hexdigest()
def sha384encrypt(string):
    sha384_object = hashlib.sha384(string.encode())
    return sha384_object.hexdigest()
def sha512encrypt(string):
    sha512_object = hashlib.sha512(string.encode())
    return sha512_object.hexdigest()
def arcfourencrypt(__str__, __key__):
    _arc4_ = ARC4(__key__)
    __result__ = _arc4_.encrypt(__str__)
    return __result__
def arcfourdecrypt(__str__, __key__):
    _arc4_ = ARC4(__key__)
    __result__ = _arc4_.decrypt(__str__)
    return __result__
if __name__ == "__main__":
    print('CoffUtils.MainStartedError')
    quit()