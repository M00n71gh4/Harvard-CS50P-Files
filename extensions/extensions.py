fileName = input("File name: ")
fileName = fileName.strip()
fileName = fileName.lower()
fileName = fileName[fileName.rfind("."):]

extentions = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip",
}

if fileName in extentions:
    print(extentions[fileName])
else:
    print("application/octet-stream")