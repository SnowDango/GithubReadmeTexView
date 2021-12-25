import subprocess
from pdf2image import convert_from_path, convert_from_bytes


class Tex2Png:

    def createPartPng(self, texFile):
        self.createPdf(texFile)
        pdfFile = texFile.replace(".tex", ".pdf")
        images = convert_from_path(pdfFile)
        partFile = 'git_md_report-part'
        print("created pdf")
        for index, image in enumerate(images):
            name = partFile + "-" + str(index) + '.png'
            image.save(name, 'png')
        return partFile

    def createPdf(self, texFile):
        for num in range(3):
            result = subprocess.run([
                "ptex2pdf",
                "-l",
                "-ot",
                "-kanji=utf8",
                "-synctex=1",
                "-file-line-error",
                "-shell-escape",
                "-interaction=nonstopmode",
                texFile
            ])
