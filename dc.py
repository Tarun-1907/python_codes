import decimal as dc

num=dc.Decimal(19.6).ln()
num0=dc.Decimal(26.08).sqrt()
print(num,"\t",num0)
print(num.compare(num0))