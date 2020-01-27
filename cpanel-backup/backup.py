import os
import time
import shutil

backup_path = '_db_backups'
mysql_path = '.mysql_backup'

def create_backup_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

file_list = os.listdir(mysql_path)
backup_list = os.listdir(backup_path)

create_backup_dir(backup_path)

for i in file_list:
    shutil.copy(mysql_path + '/' + i, backup_path + '/' + i + str(time.time()) + '.sql.gz')

for i in backup_list:
    if os.stat(os.path.join(backup_path, i)).st_mtime < time.time() - 120 * 86400:
        os.remove(os.path.join(backup_path, i))
