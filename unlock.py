import glob
import os
from cryptography.fernet import Fernet

def unlock_files():
    try:
        with open("decryption_key.key", "rb") as key_file:
            key = key_file.read()

        for locked_file in glob.glob("*.locked"):
            try:
                with open(locked_file, "rb") as file:
                    encrypted_data = file.read()
                
                cipher_suite = Fernet(key)

                decrypted_data = cipher_suite.decrypt(encrypted_data)
                original_filename = locked_file[:-7]

                with open(original_filename, "wb") as file:
                    file.write(decrypted_data)
                
                os.remove(locked_file)
                print(f"{locked_file} has been unlocked and restored to {original_filename}.")

            except Exception as e:
                print(f"Failed to unlock {locked_file}: {e}")
        
        os.remove("decryption_key.key")
    
    except Exception as e:
        print(f"Failed to load encryption key: {e}")

unlock_files()