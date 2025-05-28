import hashlib
import base64

# In-memory storage for demo
url_mapping = {}

def shorten_url(long_url):
    # Generate hash for the URL
    hash_object = hashlib.md5(long_url.encode())
    # Encode hash as base64, take first 8 chars
    short_code = base64.urlsafe_b64encode(hash_object.digest())[:8].decode()
    url_mapping[short_code] = long_url
    return short_code

# def retrieve_url(short_code):
#     # Fetch original URL from mapping
#     return url_mapping.get(short_code, "Not found")

def retrieve_url_from_short_url(short_url):
    # Extract short code from full short URL
    # Example: http://short.en/z-tkkp -> extract 'z-tkkp'
    short_code = short_url.rstrip('/').split('/')[-1]
    # Fetch original URL from mapping
    return url_mapping.get(short_code, "Not found")


# Example usage
if __name__ == "__main__":
    long_url = "https://example.com/very/long/url/12345"
    short_code = shorten_url(long_url)
    short_url = f"Short URL: http://short.en/{short_code}"
    print(f"Short URL: {short_url}")
    # print(f"Original URL: {retrieve_url(short_code)}")
    print(f"Original URL: {retrieve_url_from_short_url(short_url)}")
    print("url mapping: \n", url_mapping)
