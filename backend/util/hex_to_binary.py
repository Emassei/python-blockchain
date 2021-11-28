from backend.util.crypto_hash import crypto_hash

def hex_to_binary(hex):

   binary = bin(int(hex,16))[2:].zfill(4*len(hex))

   return binary


def main():
    number = 451
    hex_number = hex(number)[2:]
    print(f'hex_number {hex_number}')


    binary_number = hex_to_binary(hex_number)
    print(f'binary_number {binary_number}')


    original_number = int(binary_number, 2)
    print(f'original_number {original_number}')

    hex_to_binary_crypto_hash = hex_to_binary(crypto_hash('test-data'))
    print(f'hex_to_binary_crypto_hash {hex_to_binary_crypto_hash}')


if __name__ == '__main__':
    main()
