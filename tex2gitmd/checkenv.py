import platform
import shutil


class Checker:
    def envCheck(self):
        pf = platform.system()
        # tex2imgのコマンドが使えるか
        if shutil.which("ptex2pdf") is None:
            print("not found cli tool ptex2pdf")
            print("should install \"https://github.com/texjporg/ptex2pdf\"")
            exit()

    def fileCheck(self, path):
        if not path.exists():
            print(path)
            print("is not file")
            exit()
        # Texファイルかどうか
        if path.suffix != ".tex":
            print("not tex file")
            exit()
