import requests
import json
from datetime import datetime



class boampGetter:
    def __init__(self):
        self.__searchResponse = {}
        self.printAll = 0

    def __searchSize(self):
        """Return the number of ad send by Boamp.
        """
        if 'nbItemsRetournes' in self.__searchResponse:
            return self.__searchResponse['nbItemsRetournes']
        else:
            return 0
            

    def search(self,dateparution,strSearch):
        """Make a search request to Boamp.
            Store result in searchResponse.
        """
        print('Boamp search: {} after {}'.format(strSearch,dateparution))
        lineOut = 'http://api.dila.fr/opendata/api-boamp/annonces/search?criterion=dateparution>{} ET {}'.format(dateparution,strSearch)
        self.__searchResponse = requests.get(lineOut).json()
        print('{} Response found'.format(self.__searchSize()))


    def extractValidAd(self):
        """Return array of json ad wich describe the ad if date recept offer if higher tha today.
        """
        arrayReturn = []
        nbItem = self.__searchSize()
        i = 0
        while i < nbItem :
            date =0
            offre = self.__searchResponse["item"][i]
            annonce = requests.get('http://api.dila.fr/opendata/api-boamp/annonces/v230/' + offre["value"]).json()
            try:
                date = annonce['donnees']['conditiondelai']['receptoffres']
            except:
                if self.printAll:
                    print(annonce['donnees']['objet'][0]['titremarche'])
                    print(annonce['gestion']['reference']['idweb'])
                    print('\n')
            else:
                try:
                    dt_object = datetime.fromtimestamp(date/1000)
                except:
                    if self.printAll:
                        print(annonce['donnees']['objet'][0]['titremarche'])
                        print(annonce['gestion']['reference']['idweb'])
                        print('\n')
                else:
                    if self.printAll:
                        print(annonce['donnees']['objet'][0]['titremarche'])
                        print(annonce['gestion']['reference']['idweb'])
                        print(dt_object)
                        print('\n')
                    if dt_object > datetime.today():
                        arrayReturn.append(annonce)
            i+=1
        return arrayReturn;
            
