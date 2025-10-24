import os, gdown, zipfile
#https://drive.google.com/file/d/1mq3T-wiTsSU_8ucqK-2IIoJhJNKLGvlX/view?usp=drive_link
# 使用完整的文件链接
FILE_URL = "https://drive.google.com/file/d/1mq3T-wiTsSU_8ucqK-2IIoJhJNKLGvlX/view?usp=drive_link"

print("下载中...")
gdown.download(FILE_URL, "KITTI——gong.zip", quiet=False, fuzzy=True)

print("解压中...")
with zipfile.ZipFile("KITTI——gong.zip", 'r') as z:
    z.extractall(".")
os.remove("KITTI——gong.zip")

print("✓ 完成！数据集已解压到当前目录")
