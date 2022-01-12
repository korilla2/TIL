import dart_fss as dart

# Open DART API KEY 설정
api_key = 'f4af423987105c23a450a884919dec8cf35b0107'
dart.set_api_key(api_key=api_key)

# DART 에 공시된 회사 리스트 불러오기
corp_list = dart.get_corp_list()

# 삼성전자 검색
samsung = corp_list.find_by_corp_name('엔씨소프트', exactly=True)[0]

# 2012년부터 연간 연결재무제표 불러오기
fs = samsung.extract_fs(bgn_de='20220101')

# 재무제표 검색 결과를 엑셀파일로 저장 ( 기본저장위치: 실행폴더/fsdata )
fs.save()
