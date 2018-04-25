# source: https://stackoverflow.com/questions/44164829/base64-decode-specific-string-incorrect-padding-with-correct-padding

# We use hexlify for debugging.
import binascii

# We use the Base64 library.
import base64


# Base64 works on multiples of 4 characters..
# ..Sometimes we get 3/2/1 characters and it might be midway through another.
def relaxed_decode_base64(data):
    # If there is already padding we strim it as we calculate padding ourselves.
    if '=' in data:
        data = data[:data.index('=')]

    # We need to add padding, how many bytes are missing.
    missing_padding = len(data) % 4

    # We would be mid-way through a byte.
    if missing_padding == 1:
        data += 'A=='
    # Jut add on the correct length of padding.
    elif missing_padding == 2:
        data += '=='
    elif missing_padding == 3:
        data += '='

    # Actually perform the Base64 decode.
    return base64.b64decode(data)


# Debugging
print(str(relaxed_decode_base64('SFRUUC8xLjEgMTAxIFN3aXRjaGluZyBQcm90b2NvbHMNClNlcnZlcjogQXV0b2JhaG5QeXRob24vMC4xNy4yDQpVcGdyYWRlOiBXZWJTb2NrZXQNCkNvbm5lY3Rpb246IFVwZ3JhZGUNClNlYy1XZWJTb2NrZXQtQWNjZXB0OiBBUnV0a0xoenRHZ0FNd0hCSjk5UXYvcnpBa1k9DQpTZWMtV2ViU29ja2V0LUV4dGVuc2lvbnM6IHBlcm1lc3NhZ2UtZGVmbGF0ZQ0KDQqBEnsiYWN0aW9uIjogImF1dGgifQ==')) + '\n')