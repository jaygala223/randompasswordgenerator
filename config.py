import random
import string
c=[1,2,3,4,5]
b = "awqweqwdswegtr2372974358!@#!@$@#%#^&&*>?:LQWEERYOPKMNBVFCXXAZSSDFDGGGLM<BXVCBVCcnmcn,QWEWREWRTTYTRUTYIUYOPLIIKMYJHBGEDWCSQW&^*(()"
for x in range(0,5):
    c[x] = random.choice(b)
print(c)
d="".join(c)
print(d)

