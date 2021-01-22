expenses={"jan":30000,"feb":25000,"march":28000,"april":25000,"may":80000}
print(expenses["jan"])
print("june" in expenses)
expenses["june"]=49000
print(expenses)
expenses["march"]-=3000
print(expenses["march"])