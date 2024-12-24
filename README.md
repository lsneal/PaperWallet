# Bitcoin Key Generator and Paper Wallet

This Python project allows you to generate Bitcoin private and public keys, create a Bitcoin address from the public key, and convert the private key into Wallet Import Format (WIF) for wallet import. It can also generate a paper wallet containing the private key, public key, and the corresponding Bitcoin address.

## Features

### 1. Private Key Generation
The private key is generated using the **SECP256k1** elliptic curve from the `ecdsa` library. This private key is essential for generating the public key and Bitcoin address.

### 2. Public Key Generation
A public key is derived from the private key, which is used to generate the Bitcoin address.

### 3. Bitcoin Address Generation
The Bitcoin address is generated following these steps:
1. Apply **SHA-256** on the public key.
2. Apply **RIPEMD-160** on the SHA-256 result.
3. Add the **0x00** prefix (Bitcoin network identifier).
4. Generate a **checksum** (address validation) by performing **SHA-256** twice on the address with the prefix.
5. Encode the address using **Base58Check** to obtain the final Bitcoin address.

### 4. Private Key to WIF (Wallet Import Format) Conversion
The Wallet Import Format (WIF) is used to import private keys into a Bitcoin wallet. To generate a WIF key, follow these steps:
1. Add the **0x80** prefix (Bitcoin mainnet identifier).
2. Calculate the **checksum** for the private key with the prefix.
3. Encode the private key with the checksum in **Base58**.

### 5. Paper Wallet Generation
The script generates a paper wallet by printing the following details:
- The private key in WIF format.
- The public key in hexadecimal format.
- The generated Bitcoin address.