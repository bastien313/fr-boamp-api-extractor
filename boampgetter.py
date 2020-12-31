import requests
import json
from datetime import datetime

printAll = 0
searchResponse = 0

def boampSearchSize():
    """Return the number of ad send by Boamp.
    """
    try:
        nbItem = searchResponse["nbItemsRetournes"]
    except:
        return 0
    else
        return nbItem

def boampSearch(dateparution,strSearch):
    """Make a search request to Boamp.
        Store result in searchResponse.
    """
    print('Boamp search: {} after {}'.format(strSearch,dateparution))
    searchResponse = requests.get('http://api.dila.fr/opendata/api-boamp/annonces/search?criterion=dateparution>'+dateparution' ET '+strSearch).json()
    print('{} Response found'.format(boampSearchSize()))


def extractValidAd():
    """Return array of json ad wich describe the ad if date recept offer if higher tha today.
    """
    arrayReturn = []
    nbItem = boampSearchSize()
    i = 0
    while i < nbItem :
        date =0
        offre = rep["item"][i]
        annonce = requests.get('http://api.dila.fr/opendata/api-boamp/annonces/v230/' + offre["value"]).json()
        try:
            date = annonce['donnees']['conditiondelai']['receptoffres']
        except:
            if printAll:
                print(offre['description'])
                print(annonce['gestion']['reference']['idweb'])
                print('\n')
        else:
            try:
                dt_object = datetime.fromtimestamp(date/1000)
            except:
                if printAll:
                    print(offre['description'])
                    print(annonce['gestion']['reference']['idweb'])
                    print('\n')
            else:
                if printAll:
                    print(offre['description'])
                    print(dt_object)
                    print(annonce['gestion']['reference']['idweb'])
                    print('\n')
                if dt_object > datetime.today():
                    arrayReturn.append(annonce)           
    i+=1
    return arrayReturn;
        
