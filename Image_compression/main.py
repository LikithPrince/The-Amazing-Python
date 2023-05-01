
import pdb
import time
from PIL import Image
import os
from datetime import datetime


def compress(img):
    
    # pdb.set_trace()
    start=time.time()
    in_path = "images"
    path = ""
    if not os.path.exists(in_path):
        os.mkdir(in_path)

    if img:
        img1 = Image.open(img).rotate(0, expand=True)
        w,h=img1.size
        scale=0.6           #COMPRESSING %
        img2 = img1.resize((int(w*scale),int(h*scale)), Image.ANTIALIAS)

        fn = "img" + datetime.now().strftime("_%d%m%Y_%H%M%S") + ".png"
        path = os.path.join(os.getcwd(), in_path, fn)

        img2.save(path)

    print("Compression code took : ", round((time.time()-start),2), "sec")
    # return path

compress(r"C:/Users/LikithP/OneDrive - Ennoventure Inc/Documents/Projects/structured_POC/POC/Products/LotusHerbals_FMCG_1_unit_22062022_z6o_b_e1_20220625_064848/dig/enn_prod_20220625_064848.200_Lotus_whole_front_20220625_ref.png")