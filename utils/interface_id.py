from web3 import Web3
import binascii

def xor_operation(*args):
    # Create an initial buffer with 4 zero bytes
    xor_result = bytearray(4)

    for string in args:
        # Get Keccak hash using the web3 library
        keccak_digest = Web3.keccak(text=string)

        # XOR the first 4 bytes of this hash with the current xor_result
        xor_result = bytearray([a ^ b for a, b in zip(xor_result, keccak_digest[:4])])

    # Convert XOR result to a hexadecimal string
    hex_xor_result = binascii.hexlify(xor_result).decode()

    return hex_xor_result

if __name__ == "__main__":
    prompt = input("Enter interface functions and argument types -> ")
    args = tuple(prompt.split())
    xor_hex = xor_operation(*args)
    print(f"XOR of first 4 bytes of Keccak hashes: {xor_hex}")
    print("Type: ", type(xor_hex))
