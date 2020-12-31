from datetime import datetime

numerLineInAd = 4 # number of line for describe ad


class dataBase:
    def __init__(self):
        #dictionary wich contain data read in file or data to write
        #format: {'idWeb':[str1,str2....]}
        self.__dicAd = {}


    def pushAd(self, jsonDesc):
        """Push add in dicAd.
            jsonDesc is ad description supply by boamp in json format.
        """
        strList = []
        idweb = jsonDesc['gestion']['reference']['idweb']

        
        strList.append(str(jsonDesc['donnees']['objet'][0]['titremarche']))
        strList.append(str(datetime.fromtimestamp(jsonDesc['donnees']['conditiondelai']['receptoffres']/1000)))
        strList.append(idweb)


        if (idweb not in self.__dicAd):
            print('New ad in list')
            print(strList[0])
            print('Date limite: ' + strList[1])
            print('idWeb: ' + idweb + '\n')
            self.__dicAd[idweb] = strList

                         
        
    def saveAd(self, fileName):
        """Save all ad stored in __dicAd in file named by fileName
        """
        with open(fileName, "w") as fichier:
            for idweb, strList in self.__dicAd.items():
                fichier.write(strList[0] + '\n')
                fichier.write('Date limite: ' + strList[1] + '\n')
                fichier.write('idWeb: ' + idweb + '\n')
                fichier.write('------------\n')

    def loadAdd(self,fileName):
        """Load ad from file.
            overwrite all data stored in __dicAd
        """
        self.__dicAd = {}
        try:
            with open("data.txt", "r") as fichier:
                lineList = fichier.readlines()
                for idAd in range(0,len(lineList)/4):
                    self.__dicAd[lineList[(idAd*4)+0]] = [lineList[(idAd*4)+1], lineList[(idAd*4)+2], lineList[(idAd*4)+3]]
        except:
            pass
		

def getSearchWord():
    """Return list of search word
    """
    read = ''
    with open("search.txt", "r") as fichier:
        read = fichier.read()
    read = read.replace('\n',';')
    read = read.replace('\r',';')
    read = read.replace(';;',';')
    return read.split(';')
				
			
		
		

    
