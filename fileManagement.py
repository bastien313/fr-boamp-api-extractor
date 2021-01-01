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
        idweb = str(jsonDesc['gestion']['reference']['idweb'])

        strList.append(str(jsonDesc['donnees']['objet'][0]['titremarche']))
        strList.append(str(jsonDesc['donnees']['objet'][0]['objetcomplet']))
        strList.append(str(datetime.fromtimestamp(jsonDesc['donnees']['conditiondelai']['receptoffres']/1000)))

        if idweb not in self.__dicAd:
            print('New ad in list')
            print(strList[0])
            print(strList[1])
            print('Date limite: ' + strList[2])
            print('idWeb: ' + idweb + '\n')
            self.__dicAd[idweb] = strList

                         
        
    def saveAd(self, fileName):
        """Save all ad stored in __dicAd in file named by fileName
        """
        with open(fileName, 'w', encoding='utf-8') as fichier:
            for idweb, strList in self.__dicAd.items():
                fichier.write('{} \n'.format(strList[0]))
                fichier.write('{} \n'.format(strList[1]))
                fichier.write('Date limite: {}\n'.format(strList[2]))
                fichier.write('idWeb: {}\n'.format(idweb))
                fichier.write('-------------------------------------------------\n')

    def removeOldAd(self):
        """Remove all ad wich have recipient date older than today.
        """
        keyToSupr = []
        for key,val in self.__dicAd.items():
            date_time_obj = datetime.strptime(val[2], '%Y-%m-%d %H:%M:%S')
            if datetime.today() > date_time_obj:
                keyToSupr.append(key)

        for key in keyToSupr:
            print('Remove ad')
            print('{}'.format(self.__dicAd[key][0]))
            print('{}'.format(self.__dicAd[key][1]))
            print('Date limite: {}'.format(self.__dicAd[key][2]))
            print('idWeb: {}\n'.format(key))
            del self.__dicAd[key]
                
        
    def loadAdd(self,fileName):
        """Load ad from file.
            overwrite all data stored in __dicAd
        """
        self.__dicAd = {}
        try:
            with open('data.txt', 'r', encoding='utf-8') as fichier:
                read = fichier.read()
                read = read.replace('\r','')
                readTab = read.split('\n')
                for idAd in range(0,int(len(readTab)/int(5))):
                    self.__dicAd[readTab[(idAd*5)+3].replace('idWeb: ','')] = [readTab[(idAd*5)+0],
                    readTab[(idAd*5)+1],
                    readTab[(idAd*5)+2].replace('Date limite: ','')]
        except:
            pass


def getSearchWord():
    """Return list of search word
    """
    read = ''
    with open('search.txt', 'r') as fichier:
        read = fichier.read()
    read = read.replace('\n',';')
    read = read.replace('\r',';')
    read = read.replace(';;',';')
    return read.split(';')
				
			
		
		

    
