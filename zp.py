s1='abbbsbbdbbfbeweeeebrrrdssssbddd'
s2='aannbbddbffbfwefeegrrhhsshdbddd'
z_seq=zip(s1,s2)
e_seq=enumerate(z_seq)

for i,(a,b) in e_seq:
    if a!=b:
        print(f'index: {i}')