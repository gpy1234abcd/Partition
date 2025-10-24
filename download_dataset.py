import os, gdown, zipfile

FILE_ID = "你的FILE_ID"  # 

print("下载中...")
gdown.download(f"https://drive.google.com/uc?id={FILE_ID}", 
               "KITTI——gong.zip", quiet=False)

print("解压中...")
with zipfile.ZipFile("KITTI——gong.zip", 'r') as z:
    z.extractall(".")
os.remove("KITTI——gong.zip")

# print("✓ 完成！数据集在 ./VOCdevkitq/VOC2007/")
