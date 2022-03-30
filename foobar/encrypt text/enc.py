f=open('encrypt text/text.txt')
s=f.readline().strip()
print(s)
print(len(set(s)))
import base64


KEY = 'vedant.kokate'

result = []
for i, c in enumerate(base64.b64decode(s)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))