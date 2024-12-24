import hashlib
from mnemonic import Mnemonic
import hashlib
import base58
import qrcode
from ecdsa import SECP256k1, SigningKey

# Generate private key with elliptic curve SECP256k1 (esta complicado)
def generate_private_key():
    private_key = SigningKey.generate(curve=SECP256k1)
    return private_key

# Generate public key with private key
def generate_public_key(private_key):
    public_key = private_key.get_verifying_key().to_string()
    return public_key

"""
    1 -> Hash PBK -> SHA-256
    2 -> Hash res PBK -> RIPEMD-160
    3 -> Add prefix 0x00 on PBK (for network Bitcoin)
    4 -> Checksum -> x2 SHA-256 with prefix 0x00 and get first 4 bytes
    5 -> Add checksum on address for validation address
    6 -> Encode address -> Base58Check
"""
# Generate address BTC with public key
def generate_bitcoin_address(public_key):

    sha256_public_key = hashlib.sha256(public_key).digest()
    public_key_hash = hashlib.new('ripemd160', sha256_public_key).digest()
    address_bytes = b'\x00' + public_key_hash
    checksum = hashlib.sha256(hashlib.sha256(address_bytes).digest()).digest()[:4]
    address_with_checksum = address_bytes + checksum
    address = base58.b58encode(address_with_checksum).decode('utf-8')
    return address

"""
    WIF (Wallet Import Format)
    For import PVK on wallet and send coin

    1 -> Add prefix 0x80 (Identify Bitcoin Mainnet)
    2 -> Checksum -> x2 SHA-256 with prefix 0x80 and get first 4 bytes
    3 -> Add checksum on prefix 0x80 + PVK
    4 -> Encode res -> Base58
"""
def private_key_to_wif(private_key): #compressed=True):

    private_key_bytes = private_key.to_string()
    #if compressed:
    private_key_bytes += b'\x01' # for generate compressed public key 
    extended_key = b'\x80' + private_key_bytes
    checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
    extended_key_with_checksum = extended_key + checksum
    wif = base58.b58encode(extended_key_with_checksum).decode('utf-8')
    return wif

def generate_qr_code(address):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(address)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.show()

def generate_paper_wallet():
    private_key = generate_private_key()
    public_key = generate_public_key(private_key)
    address = generate_bitcoin_address(public_key)

    wif = private_key_to_wif(private_key)
    
    generate_qr_code(public_key)
    
    print(f"private_key WIF: {wif}")
    print(f"public_key: {public_key.hex()}")
    print(f"address: {address}")

generate_paper_wallet()