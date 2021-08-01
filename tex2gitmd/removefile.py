import glob
import os.path


class RemoveFile:

    def removePart(self, partFile):
        print("remove part file png:")
        for part in glob.glob(partFile + "*.png"):
            if os.path.isfile(part):
                print(part)
                os.remove(part)
        print("remove finish")
