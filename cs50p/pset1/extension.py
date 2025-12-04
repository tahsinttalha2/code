ans = input("File Name: ").lower().strip()

if ans.find(".") != -1:
    ans = ans.split('.')
    print(ans)
    i = len(ans) - 1
    if ans[i] == 'jpg' or ans[i] == 'jpeg':
        print("image/jpeg")
    elif ans[i] == 'pdf' or ans[i] == 'zip':
        print(f"application/{ans[i]}")
    elif ans[i] == 'txt':
        print("text/plain")
    elif ans[i] == 'png' or ans[i] == 'gif':
        print(f"image/{ans[i]}")
    else :
        print("application/octet-stream")
else :
        print("application/octet-stream")
