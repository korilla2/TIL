import dart_fss as dart

api_key = 'f4af423987105c23a450a884919dec8cf35b0107'
dart.set_api_key(api_key=api_key)

# 2021년 1월 1일부터 2021년 3월 31일까지 검색
reports = dart.filings.search(bgn_de='20210101', end_de='20210331')

print(reports)
