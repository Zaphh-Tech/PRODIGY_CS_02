# My Prodigy Task 2 - Image Encryption

Encrypts images by shifting each pixel value. Same key decrypts it back.

Encrypt: each R,G,B + key (mod 256). Decrypt: minus key. Alpha channel left alone.

## how to run

```
pip install Pillow

python3 image_encrypt.py --encrypt --input in.png --output enc.png --key 42
python3 image_encrypt.py --decrypt --input enc.png --output dec.png --key 42
```

Use the same key both times or it wont decode right.

Can also use it in python:
```python
from image_encrypt import encrypt_image, decrypt_image
encrypt_image("in.png", "enc.png", 42)
decrypt_image("enc.png", "dec.png", 42)
```

## files

- `image_encrypt.py`
- `test_images/` - my test pics (original, encrypted, decrypted)

Its just a learning exercise, not real secure encryption.
