#globals()#是将变量转换为全局变量
#nonlocal()#是将局部变量转换为全局变量
#shutil.copyfile(file, file)前者复制到后者
import logging
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
