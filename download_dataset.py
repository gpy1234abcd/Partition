import os, gdown, zipfile

FILE_ID = "你的FILE_ID"  # 

print("下载中...")
gdown.download(f"https://drive.google.com/uc?id={FILE_ID}", 
               "VOC2007.zip", quiet=False)

print("解压中...")
with zipfile.ZipFile("VOC2007.zip", 'r') as z:
    z.extractall(".")
os.remove("VOC2007.zip")

print("✓ 完成！数据集在 ./VOCdevkitq/VOC2007/")
