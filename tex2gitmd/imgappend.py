import os

from PIL import Image
import glob

class ImgAppend:

    def pngAppend(self, partFile):
        im_list = []

        for filename in sorted(glob.glob(partFile + '-*.png'), key=os.path.getmtime):
            im_list.append(Image.open(filename))

        afterIm = Image.new("RGB", (im_list[0].width, im_list[0].height * len(im_list)))
        for i in range(len(im_list)):
            afterIm.paste(im_list[i], (0, im_list[0].height * i))
        afterIm.save("git_md_report.png")
