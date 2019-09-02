a = ['1','1','1','0','1','1','1']
tmp = ''.join(a).split('0').count('1'*3)
print(tmp)