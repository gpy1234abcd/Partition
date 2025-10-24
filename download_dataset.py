import os, gdown, zipfile
#https://drive.google.com/file/d/1mq3T-wiTsSU_8ucqK-2IIoJhJNKLGvlX/view?usp=drive_link
FILE_ID = "1mq3T-wiTsSU_8ucqK-2IIoJhJNKLGvlX"

print("下载中...")
gdown.download(f"https://drive.google.com/uc?id={FILE_ID}", 
               "KITTI——gong.zip", quiet=False)

print("解压中...")
with zipfile.ZipFile("KITTI——gong.zip", 'r') as z:
    z.extractall(".")
os.remove("KITTI——gong.zip")

print("✓ 完成！数据集已解压到当前目录")
