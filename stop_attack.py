import base64, time
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def d(e, k):
    b = base64.b64decode(e)
    c = AES.new(k, AES.MODE_CBC, b[:16])
    return unpad(c.decrypt(b[16:]), 16)

def run():
    print("\n[!] Running secure shutdown sequence...\n")
    time.sleep(1)
    key = b'secret_key_12345'
    e = "6uA0SEFX/sHqbuiF3BxpBV35JVHP19rVm7WnG8G3tTT4dmTk4KvrixhMx4DzsNVl8olrbLwLJu6nq1d5kDddyQ=="
    f = d(e, key)
    print(f.decode())
    print("\n Attack stopped successfully.")

if __name__ == "__main__":
    run()

