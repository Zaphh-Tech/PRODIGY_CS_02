# PRODIGY_CS_02

An image encryption tool written in Python, built for Task 2 of the Prodigy InfoTech
Cyber Security internship.

It scrambles an image by shifting every pixel value with a key, and the same key
shifts it back to the original.

## What it does

- Encrypts and decrypts images by adding/subtracting a key on each pixel (mod 256)
- Works on RGB and RGBA images (the alpha channel is left alone)
- Round-trips exactly — decrypting with the same key gives back the original
- Can be used from the command line or imported as functions

## Setup

```bash
pip install Pillow
```

## How to run

```bash
python3 image_encrypt.py --encrypt --input in.png --output enc.png --key 42
python3 image_encrypt.py --decrypt --input enc.png --output dec.png --key 42
```

Use the same key both ways or it won't decode.

As a module:

```python
from image_encrypt import encrypt_image, decrypt_image
encrypt_image("in.png", "enc.png", 42)
decrypt_image("enc.png", "dec.png", 42)
```

## Example output

```
$ python3 image_encrypt.py --encrypt --input in.png --output enc.png --key 42
image encrypted: in.png -> enc.png
```

## Files

- `image_encrypt.py` — the tool
- `test_images/` — sample pics (original, encrypted, decrypted)

This is a learning exercise, not real secure encryption.
