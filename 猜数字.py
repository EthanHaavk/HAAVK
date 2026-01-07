import random
k=str(random.randint(1,10))
if input('猜一猜1-10:')==k:
    print('对啦')
else:
    print('猜错啦，我想的是'+k)
