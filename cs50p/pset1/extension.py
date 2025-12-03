ans = input().lower().strip()

ans = ans.split('.')
if ans[1] == 'jpg' or ans[1] == 'jpeg':
    print("image/jpeg")
elif ans[1] == 'pdf' or ans[1] == 'zip':
    print(f"application/{ans[1]}")
elif ans[1] == 'txt':
    print("text/plain")
elif ans[1] == 'png' or ans[1] == 'gif':
    print(f"image/{ans[1]}")
else :
    print("application/octet-stream")