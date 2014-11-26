# -*- coding: utf-8 -*-
'''
Created on 2014. 9. 15.

@author: dulee
'''


def get_help():
	return """
=================================================================
== 도움말
=================================================================
<< 테이블 목록 >>
select * from TN_BUF_DISEN                        : 연결체
select * from TN_BUF_DISEN_IVINF                  : 연결체 개인정보
select * from TN_SPB_REQST_BUF_PRDCTN_QY
select * from TN_SPB_REQST_BUF                    : 신청
select * from TN_SPB_REQST
select * from TN_SPB_REQST_IVINF
select * from TN_SPB_REQLAND_BUF_FEED_CROPS
select * from TN_SPB_REQLAND_BUF
select * from TN_SPB_REQLAND_FLFLCK_BUF
select * from TN_SPB_REQLAND_FLFLCK
select * from TN_AGBS_PSTD_BUF                    : 조사료 지급기준
select * from TN_AGBS_PSTD                        : 지급기준
select * from TC_AGBS_CMMNCODE                    : 공통코드 테이블.
select * from TN_SPB_REQST_PAPERS                 : 신청인 서류.
select * from ACM_COMMONCODE_T                    : 전체공통
select * from TN_AGBS_PROGRS_SSN                  : 농림사업진행절기.
select * from TN_AGBS_PROGRS                      : 농림사업진행
select * from BA_BZOB_BSE_I A                     : 신청서경영체기본정보  
select * from BA_BZOB_BSE_D B                     : 신청서경영체기본상세
select * from BA_BZOB_AGRM_S                      : 신청서경영체농업인명세
select * from CM_COMMONCODE_VW@UNIFARM_LN	      : 공통코드



<< 데이터 셋 상태 >>
Dataset.getRowType(nRow)
Dataset.ROWTYPE_EMPTY	0	존재하지 않는 행의 상태
Dataset.ROWTYPE_NORMAL	1	초기 행의 상태
Dataset.ROWTYPE_INSERT	2	추가된 행의 상태
Dataset.ROWTYPE_UPDATE	4	수정된 행의 상태
Dataset.ROWTYPE_DELETE	8	삭제된 행의 상태
Dataset.ROWTYPE_GROUP	16	그룹 정보 행의 상태
<< 코드 템플릿 >>
private Logger log = Logger.getLogger(getClass());

@Resource(name = "c2020101.BufVoUtilCamelDs") 
private BufVoUtilIf voUtilCamel;
	
@Resource(name = "c2020101.BufVoUtilUnderscoreDs") 
private BufVoUtilIf voUtilUnderscore;
	
public String toString() {
	return ToStringBuilder.reflectionToString(this);
}

리사이징 할때 .grid 속성중 autofitype는 col 로 해주세요..그래야 그리드 까지 됩니다...
"""



if __name__ == '__main__':
	pass