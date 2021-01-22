pattern="ABCABBAAEEEEEE"
dict={}
for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        break
print(ch,"first recursive character")