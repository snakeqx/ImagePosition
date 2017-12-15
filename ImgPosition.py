from bat.DatabaseHandler import SQL3Handler
from bat.DirectoryHandler import DirectoryHandler
from bat.ImageHandler import ImageHandler
import logging
import sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=r'./BatPlus.log',
                    filemode='w')
# define a stream that will show log level > Warning on screen also
console = logging.StreamHandler()
console.setLevel(logging.WARNING)
formatter = logging.Formatter('%(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

if __name__ == '__main__':
    files = DirectoryHandler(r'/Users/qianxin/Downloads/108054fail')
    fp = open("test.txt", 'w')
    fp.write("System SN,Scan Mode,Center Col,Center Row,mm/pix,phantom radius\n")

    count = 1
    for _file in files.Dicom_File_Path:
        sys.stdout.write(f"\rAnalyzing {count:d} / {files.Total_Dicom_Quantity:d} dicom files")
        _image = ImageHandler(_file)
        count += 1
        if _image.isImageComplete:
            fp.write(_image.SerialNumber + ',' +
                     _image.ScanMode + ',' +
                     str(_image.Center[0]) + ',' +
                     str(_image.Center[1]) + ',' +
                     str(_image.PixSpace[0]) + ',' +
                     str(_image.Radius[1]) + '\n')

    fp.close()
