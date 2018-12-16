import gzip
import shutil


def unzip_gz_file(inputfile, outputfile, filename):
    inf = gzip.open(inputfile+"/"+filename, 'rb')
    file_content = inf.read()
    inf.close()
    opf = open(outputfile+"/"+filename[:-3], "wb")
    opf.write(file_content)
    opf.close()

    '''with gzip.open(inputfile+"/"+filename, 'rb') as f_in:
        with open(outputfile+"/"+filename[:-3], 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)'''


# unzip_gz_file("C:/Users/AF86407/Desktop/PegaLogAnalyzer/Logs", "C:/Users/AF86407/Desktop/PegaLogAnalyzer/Logs", "PegaRULES-10-29-2018-1.log.gz")