import os
class checkpoint:
    allow_different_dimensions = False
    batch_size = 4
    checkpoint_dir = '../ImagesDB/checkpoints/8'
    device = '/gpu:0'
    in_path1 = '../ImagesDB/input/'
    in_path = ""
    out_path = '/home/hadoop/Documents/fast-style-transfer-master/examples/output/8.jpg'
    def handle(self):
        for i in os.listdir(self.in_path):
            # print(os.getcwd())
            self.in_path=self.in_path+i
            # print(self.in_path)

if __name__ == '__main__':
    a=checkpoint()
    a.handle()
