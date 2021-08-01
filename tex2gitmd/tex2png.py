import platform
import subprocess


class Tex2Png:

    def createPartPng(self, texFile):
        global result
        partFile = 'git_md_report-part'
        if platform.system() == 'Darwin':
            result = subprocess.run(
                ['tex2img', '--keep-page-size', '--with-text', '--no-transparent', '--kanji=utf8', texFile,
                 partFile + '.png'])
        elif platform.system() == 'Windows':
            result = subprocess.run(
                ['tex2imgc', '--keep-page-size', '-with-text', '--no-transparent', '--kanji=utf8', texFile,
                 partFile + '.png'])
        if result.returncode == 1:
            print("Sorry. tex2img error.")
            exit()
        return partFile
