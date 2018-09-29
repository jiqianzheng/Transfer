import os
import checkpoint_1
from utils import  main


def get_image():
          input_path="/home/hadoop/Documents/jqzh/transfer_test_image/input/"

          out_path = "/home/hadoop/Documents/jqzh/transfer_test_image/output/"
          i = checkpoint_1
          a = i.checkpoint()
          print("修改checkpoint参数******--------------")
          print(os.getcwd())
#          设置跑的模型范围
          for type in range(18,19):
              if type in [10,12]:
                  continue
              else:
                  a.checkpoint_dir = os.path.join(a.checkpoint_dir1, str(type))
                  for file_name in os.listdir(input_path):
                      print(file_name)
                      for image_name in os.listdir(os.path.join(input_path,file_name)):
                          print(image_name)
                          a.in_path=os.path.join(os.path.join(input_path,file_name),image_name)
                          image_path=os.path.join(out_path,str(type),file_name)
                          isExits=os.path.exists(image_path)
                          if not isExits:
                              os.makedirs(image_path)
                          a.out_path=os.path.join(image_path,image_name)
                          main(a)
                          print("修改完成******--------------")
                  # a.in_path = save_path
                  # a.out_path = os.path.join(a.out_path1)
                  # print("*******************",os.path.join(out_path,data.filename))
                  #
                  # print('a.checkpoint_dir:',a.checkpoint_dir)
                  # print(a.in_path)
                  # print(a.out_path)
                  # main(a)
                  # print("修改完成******--------------")

if __name__ == '__main__':
    get_image()












































