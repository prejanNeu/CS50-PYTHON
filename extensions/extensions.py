filename = input("Enter filename: ").lower().strip()
parts = filename.split(".")

if parts[-1] == "jpg" or parts[-1] == "jpeg":
    print("image/jpeg")
elif parts[-1] == "zip" or parts[-1] == "pdf":
    print("application/" + parts[-1])
elif parts[-1] == "txt":
    print("text/plain")
elif parts[-1] == "png" or parts[-1] == "gif":
    print("image/" + parts[-1])
else:
    print("application/octet-stream")
