#!/usr/bin/env python3
"""UUID v4 generator — random UUID per RFC 4122."""
import os
def uuid4():
    b=bytearray(os.urandom(16))
    b[6]=(b[6]&0x0F)|0x40  # version 4
    b[8]=(b[8]&0x3F)|0x80  # variant 1
    h="".join(f"{x:02x}" for x in b)
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:]}"
def parse_uuid(s):
    s=s.replace("-","")
    if len(s)!=32:raise ValueError("Invalid UUID")
    return bytes.fromhex(s)
def uuid_version(s):
    b=parse_uuid(s);return(b[6]>>4)&0x0F
def main():
    for _ in range(3):u=uuid4();print(f"{u} (v{uuid_version(u)})")
if __name__=="__main__":main()
