# image encryption with pixel shifting - prodigy task 2
# encrypt adds key to every pixel, decrypt subtracts it back

import argparse
import sys

try:
    from PIL import Image
except ImportError:
    print("need Pillow: pip install Pillow")
    sys.exit(1)


def do_image(input_path, output_path, key, encrypt=True):
    key = int(key) % 256
    try:
        img = Image.open(input_path)
    except FileNotFoundError:
        print("file not found:", input_path)
        sys.exit(1)
    except OSError as e:
        print("cant open image:", e)
        sys.exit(1)

    if img.mode == "RGBA":
        img = img.convert("RGBA")
        px = list(img.getdata())
        if encrypt:
            new = [((r + key) % 256, (g + key) % 256, (b + key) % 256, a) for (r, g, b, a) in px]
        else:
            new = [((r - key) % 256, (g - key) % 256, (b - key) % 256, a) for (r, g, b, a) in px]
        out = Image.new("RGBA", img.size)
        out.putdata(new)
    else:
        if img.mode != "RGB":
            img = img.convert("RGB")
        px = list(img.getdata())
        if encrypt:
            new = [((r + key) % 256, (g + key) % 256, (b + key) % 256) for (r, g, b) in px]
        else:
            new = [((r - key) % 256, (g - key) % 256, (b - key) % 256) for (r, g, b) in px]
        out = Image.new("RGB", img.size)
        out.putdata(new)

    out.save(output_path)
    word = "encrypted" if encrypt else "decrypted"
    print("image " + word + ": " + input_path + " -> " + output_path)
    return output_path


def encrypt_image(input_path, output_path, key):
    return do_image(input_path, output_path, key, encrypt=True)


def decrypt_image(input_path, output_path, key):
    return do_image(input_path, output_path, key, encrypt=False)


# short name too
decrypt = decrypt_image
encrypt = encrypt_image


def main(argv=None):
    p = argparse.ArgumentParser(description="image encrypt/decrypt by shifting pixels")
    m = p.add_mutually_exclusive_group(required=True)
    m.add_argument("--encrypt", action="store_true")
    m.add_argument("--decrypt", action="store_true")
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--key", required=True, type=int)
    a = p.parse_args(argv)
    if a.encrypt:
        encrypt_image(a.input, a.output, a.key)
    else:
        decrypt_image(a.input, a.output, a.key)


if __name__ == "__main__":
    main()
