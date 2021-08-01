import sys
from pathlib import Path

from tex2gitmd.checkenv import Checker
from tex2gitmd.imgappend import ImgAppend
from tex2gitmd.tex2png import Tex2Png
from tex2gitmd.removefile import RemoveFile


# argv[1] = tex
# argv[2] = output


def main(argv=sys.argv[1:]):

    if sys.argv[1] == "-h" or sys.argv[1] == "--help" or sys.argv[1] == "help":
        print("Usage: \n\t tex2gitmd texfile [options]")
    else:
        if len(sys.argv) == 3:
            if sys.argv[2] != "-p" and sys.argv[2] != "--part":
                print("option error")
                exit()
        elif len(sys.argv) > 3:
            print("option error")
            exit()

        # 環境check
        checker = Checker()
        checker.envCheck()
        texPath = Path(sys.argv[1])
        checker.fileCheck(texPath)

        # tex to png convert
        tex2png = Tex2Png()
        partFileName = tex2png.createPartPng(sys.argv[1])

        if len(sys.argv) == 2:
            # imageの連結
            imgAppender = ImgAppend()
            imgAppender.pngAppend(partFileName)

            # part fileの削除
            removeFile = RemoveFile()
            removeFile.removePart(partFileName)

        # 終了
        print("complete !! \nplease write ")


