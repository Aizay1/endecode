#!/usr/bin/env python3

import urllib.parse
import html
import base64
import codecs

def url_encode(text):
    return urllib.parse.quote(text)

def url_decode(text):
    return urllib.parse.unquote(text)

def html_encode(text):
    return html.escape(text)

def html_decode(text):
    return html.unescape(text)

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    return base64.b64decode(text).decode()

def utf8_encode(text):
    return text.encode("utf-8")

def utf8_decode(text):
    return text.decode("utf-8")

def hex_encode(text):
    return text.encode().hex()

def hex_decode(text):
    return bytes.fromhex(text).decode()

def binary_encode(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_decode(text):
    return ''.join(chr(int(b, 2)) for b in text.split())

def rot13_encode(text):
    return codecs.encode(text, 'rot_13')

def rot13_decode(text):
    return codecs.decode(text, 'rot_13')

if __name__ == "__main__":
    print("Welcome to Encode/Decode Tool!")
    print("Choose an operation:")
    print("1. Encode")
    print("2. Decode")
    operation = input("Enter your choice (1 or 2): ").strip()

    if operation not in ['1', '2']:
        print("Invalid choice. Exiting.")
        exit()

    print("\nChoose the type:")
    print("1. HTML")
    print("2. URL")
    print("3. Base64")
    print("4. UTF-8")
    print("5. Hexadecimal")
    print("6. Binary")
    print("7. ROT13")
    encoding_type = input("Enter your choice (1-7): ").strip()

    if encoding_type not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Invalid choice. Exiting.")
        exit()

    text = input("\nEnter the text: ")

    try:
        if operation == '1':  # Encode
            if encoding_type == '1':
                print("Encoded (HTML):", html_encode(text))
            elif encoding_type == '2':
                print("Encoded (URL):", url_encode(text))
            elif encoding_type == '3':
                print("Encoded (Base64):", base64_encode(text))
            elif encoding_type == '4':
                print("Encoded (UTF-8):", utf8_encode(text))
            elif encoding_type == '5':
                print("Encoded (Hex):", hex_encode(text))
            elif encoding_type == '6':
                print("Encoded (Binary):", binary_encode(text))
            elif encoding_type == '7':
                print("Encoded (ROT13):", rot13_encode(text))
        elif operation == '2':  # Decode
            if encoding_type == '1':
                print("Decoded (HTML):", html_decode(text))
            elif encoding_type == '2':
                print("Decoded (URL):", url_decode(text))
            elif encoding_type == '3':
                print("Decoded (Base64):", base64_decode(text))
            elif encoding_type == '4':
                print("Decoded (UTF-8):", utf8_decode(text.encode()))
            elif encoding_type == '5':
                print("Decoded (Hex):", hex_decode(text))
            elif encoding_type == '6':
                print("Decoded (Binary):", binary_decode(text))
            elif encoding_type == '7':
                print("Decoded (ROT13):", rot13_decode(text))
    except Exception as e:
        print(f"Error: {e}")
