# DocumentLocker

DocumentLocker is a Python-based file encryption and decryption tool designed to lock and unlock `.doc` files securely. This project is intended for educational purposes to demonstrate basic cryptographic operations and file handling, and it should not be used for malicious purposes.

## Features
- Encrypts all `.doc` files in the current directory.
- Decrypts all locked files in the current directory using a generated key.
- Securely handles encryption keys.

## Requirements
- Python 3.x
- cryptography module

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/DocumentLocker.git
    cd DocumentLocker
    ```

2. Install the required packages:
    ```sh
    pip install cryptography
    ```

## Usage

### Encrypt Files
To encrypt all `.doc` files in the current directory, run:
```sh
python lock_files.py
```

### Decrypt Files
To decrypt all locked files in the current directory, run:
```sh
python unlock_files.py
```
