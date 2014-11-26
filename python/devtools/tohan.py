# -*- coding: utf-8 -*-
'''
Created on 2014. 8. 27.
단어사전 기반으로 영문을 한글로 변경하는 모듈.
'''
import util




mydict = util.load_file("dict.txt")

#print mydict['CD']


s = "SAUP_CD,GTCAT_CD,GTCAT_NM,MDSAUPCAT_CD,MDSAUPCAT_NM,LTSAUPCAT_CD,LTSAUPCAT_NM,DESAUPCAT_CD,SAUP_NM,ONLINE_GB,UNIT_SYSTEM_GB,SYSTEM_GB,FARM_BIZ_GB,USE_GB,SEQ,REG_ID,REG_DT,XP_SYSTEM_GB,XP_LAUNCHING_URL"

names = s.split(',')


print
print s
print util.eng_to_han(mydict, names)