import platform
import shutil


class Checker:
    def envCheck(self):
        pf = platform.system()
        # tex2imgのコマンドが使えるか
        if pf == 'Darwin':
            if shutil.which("tex2img") is None:
                print("not found cli tool tex2img")
                print("should install \"https://tex2img.tech/\"")
                exit()
        elif pf == 'Windows':
            if shutil.which("tex2imgc") is None:
                print("not found cli tool tex2imgc")
                print("should install \"https://tex2img.tech/\"")
                exit()
        elif pf == 'Linux':
            print("Sorry. Not supported")
            exit()

    def fileCheck(self, path):
        if not path.exists():
            print(path + " is not file")
            exit()
        # Texファイルかどうか
        if path.suffix != ".tex":
            print("not tex file")
            exit()
