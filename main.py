import fileManagement as fm
import boampgetter as boamp

database = fm.dataBase()
bmgt = boamp.boampGetter()
bmgt.printAll = 0
database.loadAdd('data.txt')

searchList = fm.getSearchWord()

for searchWord in searchList:
	bmgt.search('2020/11/01',searchWord)
	#boamp.boampSearch('2020/10/01','')
	adList = bmgt.extractValidAd()
	for ad in adList:
		database.pushAd(ad)
		
database.saveAd('data.txt')
