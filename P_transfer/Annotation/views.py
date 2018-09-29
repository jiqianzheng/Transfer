from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from .utils import write2disk
import  os
from PIL import Image
from .utils import main
from checkpoints import  checkpoint_1,checkpoint_2,checkpoint_3,checkpoint_4,checkpoint_5,checkpoint_6,checkpoint_7,checkpoint_8
# Create your views here.
from django.template.loader import render_to_string
# 图片上传
import  c_input
def get_classify_image(request):
    """
    保存上传图像
     """
    response = {"status": 0}
    if request.method == "POST":
        file_data= request.FILES.get(r"image", "没有图片")
        # print("************************************************")
        img = Image.open(file_data)
        file_path=os.path.join('./ImagesDB','input')
        # print(file_path)
        file_data_Url=os.path.join(file_path,file_data.name)
        write2disk(file_path, file_data_Url, img)
    return JsonResponse(response)


def process_classify(request):
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&")
    pass
def process_classify_1_by_1(request):
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(os.getcwd())
    input_file='./ImagesDB/input/'
    i=checkpoint_1
    a=i.checkpoint()
    print("修改checkpoint参数******--------------")
    for i in range(1,9):
        print(os.getcwd())
        a.checkpoint_dir =os.path.join(a.checkpoint_dir1,str(i))
        for j in os.listdir(input_file):
            a.in_path=os.path.join(a.in_path1,j)
            key=j[-4:]
            a.out_path = os.path.join(a.out_path1, str(str(i)+key))

        print(a.checkpoint_dir)
        print(a.in_path)
        print(a.out_path)
        main(a)
    print("修改完成******--------------")
    result=['finished processing']
    return HttpResponse("".join(result))


def index(request):
    return render(request,'index.html')

def classify(request):
    return render(request,"classify.html")
def classify_show(request):
    input_file = './ImagesDB/input/'
    for j in os.listdir(input_file):
         return render(request, "classify_show.html",{"file_name":j})


def show(request):
    return render(request,'show.html')



