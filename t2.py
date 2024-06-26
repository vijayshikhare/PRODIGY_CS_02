from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    image = Image.open(image_path)
    # Convert image to numpy array
    image_array = np.array(image)
    
    # Encrypt the image by adding the key value to each pixel
    encrypted_array = (image_array + key) % 256
    
    # Convert encrypted array back to image
    encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))
    
    return encrypted_image

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    # Convert image to numpy array
    encrypted_array = np.array(encrypted_image)
    
    # Decrypt the image by subtracting the key value from each pixel
    decrypted_array = (encrypted_array - key) % 256
    
    # Convert decrypted array back to image
    decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))
    
    return decrypted_image

# Example usage:
# Encrypting the image
key = 50  # Example key value for encryption
image_path = 'nature.png'
encrypted_image = encrypt_image(image_path, key)
encrypted_image.save('encrypted_image.png')

# Decrypting the image
encrypted_image_path = 'encrypted_image.png'
decrypted_image = decrypt_image(encrypted_image_path, key)
decrypted_image.save('decrypted_image.png')
