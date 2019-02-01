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

if __name__ == '__main__':
    print("Popula Script start")
    unzip_gz_file("//va10papnas005b.us.ad.wellpoint.com/IngenioRx/IPS/DEV/Prod/Logs/IPS-PROD-Logs/322","//va10papnas005b.us.ad.wellpoint.com/IngenioRx/IPS/DEV/Prod/Logs/IPS-PROD-Logs/322","PegaRULES-01-13-2019-1.log.gz")
    # get_PyElement()
    print("Popula Script end")