import hashlib
import json

def crypto_hash(*args):
    """
    Return a sha-256 hash of the given arguments
    """
    stringified_data = sorted(map(lambda data: json.dumps(data), args))
    joined_data = ''.join(stringified_data)
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash(1,'two','three'):{crypto_hash(1,'two','three')}")
    print(f"crypto_hash('two',1, 'three'):{crypto_hash('two',1, 'three')}")


if __name__ == '__main__':
    main()
