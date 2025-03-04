""" 
Hashable
"""
import hashlib
import json

def crypto_hash(*args):
    """ 
    Return a sha-256 hash
    """
    str_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = ''.join(str_args)
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()
    

def main():
    pass

if __name__ == '__main__':
    main()