# today we are gonna learn some dictionary methods!!
# lets do this

S1  = {'shivesh': 100 , 'isha': 90 , 'sharma':-10 , 'nimki':70} 
# this is section 1 students marks

S2 = {'lakshy': 00 , 'shreyas': 40 , 'prince':30 , 'shukla':40}
# this is section 2 students marks

S1.update(S2)
print(S1)
S1.popitem()
print(S1)
S1.pop('sharma')
print(S1)
S1.clear()
print(S1)
