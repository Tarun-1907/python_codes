import re
s="Hello everyone, this is regular expression."
charrs=re.findall("[h-v]",s)
print(charrs)