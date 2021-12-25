import os
import pathlib

from PIL import Image
import glob

class ImgAppend:

    def pngAppend(self, partFile):
        im_list = [Image.open(partFile + ".png")]
        for partFileName in sorted(glob.glob('*.png'), key=os.path.getmtime):
            if len(im_list) == 1:
                continue
            im_list.insert(len(im_list), Image.open(partFileName))

        afterIm = Image.new("RGB", (im_list[0].width, im_list[0].height * len(im_list)))
        for i in range(len(im_list)):
            afterIm.paste(im_list[i], (0, im_list[0].height * i))
        afterIm.save("git_md_report.png")
