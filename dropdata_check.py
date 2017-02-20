import sys
import requests
import time


if len(sys.argv) < 5:
    print("[url] [lines per entry] [outfile] [time between checks]")
    sys.exit()



while 1:
    outfilen = open(sys.argv[3], "a+")
    loggen = requests.get(sys.argv[1], stream=True)
    slut_linje = int(sys.argv[2])
    progress = 0
    collected_line = ""
    for line in loggen.iter_lines():
        if progress == slut_linje:
            progress = 0
            collected_line = collected_line+str(line).replace("b'","").replace("'","")+";"
            outfilen.write(collected_line+"\n")
            collected_line = ""
        else:
            collected_line = collected_line+str(line).replace("b'","").replace("'","")+";"
            progress = progress+1
    outfilen.close()
    print("File saved")
    time.sleep(int(sys.argv[4]))
