import fileManagement as fm
import boampgetter as boamp

database = fm.dataBase()
bmgt = boamp.boampGetter()
bmgt.printAll = 0
database.loadAdd('data.txt')
database.removeOldAd()

#bmgt.saveJsonFile('20-152081')


#searchList = fm.getSearchWord()

#for searchWord in searchList:
#	bmgt.search('2020/11/01',searchWord)
#	adList = bmgt.extractValidAd()
#	for ad in adList:
#		database.pushAd(ad)
		
database.saveAd('data.txt')
