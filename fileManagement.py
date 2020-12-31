



class dataBase:
    def __init__(self):
        # dictionary wich contain data read in file or data to write
        #format: {'idWeb':[str1,str2....]}
        __dicAd = {}


    def pushAd(self, jsonDesc):
        """Push add in dicAd.
        jsonDesc is ad description supply by boamp in json format.
        """
        strList = []
        idweb = jsonDesc['gestion']['reference']['idweb']
        
        strList.pushBack(jsonDesc['description']
        strList.pushBack(jsonDesc['description'])
        strList.pushBack(idweb)


        if (idweb not in self.__dicAd):
            dicAd[idweb] = strList
            print('New ad in list')
            print(strList[0])
            print('Date limite: ' + jsonDesc['description'])
            print('idWeb: ' + idweb + '\n')
            self.__dicAd[idweb] = strList

                         
        
    def saveAd(self, fileName):
    """Save all ad stored in __dicAd in file named by fileName
    """
        file = fopen(fileName,'w')

        for idweb, strList in self.__dicAd.items():
            fichier.write(strList[0] + '\n')
            fichier.write('Date limite: ' + strList[1] + '\n')
            fichier.write('idWeb: ' + idweb + '\n')
            fichier.write('------------\n')

    def loadAdd(self,fileName):
        """Load ad from file.
            overwrite all data stored in __dicAd
        """
        __dicAd = {}
        fileRead = 0
        with open("data.txt", "r") as fichier:
            fileRead = fichier.read()

    
