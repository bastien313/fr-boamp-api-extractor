from datetime import datetime
import json

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

                    
    def saveAd(self):
        """Save all ad in file ad.json
        """
        with open('ad.json', 'w') as outfile:
            json.dump(self.__dicAd, outfile)

    def loadAdd(self):
        """Load ad from ad.json file.
            overwrite all data stored in __dicAd
        """
        try:
            with open('ad.json', 'r') as json_file: 
                self.__dicAd = json.load(json_file)
        except:
            pass

    
    def adIsReject(self, ad, rejectedWord = []):
        """Check if ad must be reject or valid.
            Return 1 if ad must be reject.
        """
        for word in rejectedWord:
            if word in ad[0] or word in ad[1]:
                return 1
        return 0
        
    def makeOutputFile(self, fileName, fileNameReject, rejectedWord = []):
        """Write all not rejected ad in filename and all rejected ad in fileNameReject.
            rejectedWord is the list of word for reject offer
        """

        fileValid = open(fileName, 'w', encoding='utf-8')
        fileReject = open(fileNameReject, 'w', encoding='utf-8')
        fileOut = 0
        for idweb, strList in self.__dicAd.items():
            if self.adIsReject(strList, rejectedWord):
                fileOut = fileReject
            else:
                fileOut = fileValid
                
            fileOut.write('{} \n'.format(strList[0]))
            fileOut.write('{} \n'.format(strList[1]))
            fileOut.write('Date limite: {}\n'.format(strList[2]))
            fileOut.write('idWeb: {}\n'.format(idweb))
            fileOut.write('-------------------------------------------------\n')
            

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

def getWordList(fileNme):
    """Return list of line writen in file and skip '\n' '\r'
    """
    read = ''
    with open(fileNme, 'r') as fichier:
        read = fichier.read()
    read = read.replace('\n',';')
    read = read.replace('\r',';')
    read = read.replace(';;',';')
    
    lineOut = []
    for line in read.split(';'):
        if line != '':
            lineOut.append(line)
    return lineOut
            
				
			
		
		

    
