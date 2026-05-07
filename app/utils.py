import hashlib

def generate_short_code(url:str)->str:
    short_code =  hashlib.sha256(url.encode()).hexdigest()[:8]
    return short_code

