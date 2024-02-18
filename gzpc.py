import gzip
s=b'Hello World'
print(len(s))

m=gzip.compress(s)
print(len(m))