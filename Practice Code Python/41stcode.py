import os
if not os.path.exists("100dayscodetrial"):
    os.mkdir("100dayscodetrial")
    
for i in range (1 , 101):
    with open(f"100dayscodetrial/{i+1}.py" , "w") as tested:
        #  os.rename(f"100dayscodetrial/{i+1}.py" , f"100dayscodetrial/{i+1}thcode.py")
        pass