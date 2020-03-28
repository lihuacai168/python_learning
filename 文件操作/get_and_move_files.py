# -*- coding: utf-8 -*-
import os
import sys


# 获取文件路径
path = sys.argv[0]

# aria2传过来的第二个参数,文件数量,第三个是文件夹名称
file_num = sys.argv[1]

# downloadpath=默认下载路径
downloadpath='/usr/local/caddy/www/aria2/Download'

rclone='/home/lihuacai168/gdrive_unlimit/TW_aria2_Download'

if file_num != 0:

    # 获取最新下载文件
    last_file_cmd = "file=ls -t %s|head -1%(downloadpath)"
    print("获取最新下载文件命令: "+last_file_cmd)

    last_file = os.system(last_file_cmd)
    print("获取最新下载文件 : "+last_file)



    # 把最新下载的文件移动到挂载路径
    mv_file_cmd = "mv -f %s/%s %s"%(downloadpath,last_file,rclone)
    print("把最新下载的文件移动到挂载路径  "+mv_file_cmd)

    os.system(mv_file_cmd)