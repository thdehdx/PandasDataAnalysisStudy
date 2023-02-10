#F9를 누르면 선택한 구역 실행
#데이터 과학자를 위한 판다스
#시리즈 : 1차원 데이터 형식
#데이터프레임 : 2차원 데이터 형식

#예제 1-1 딕셔너리->시리즈 변환
# pandas 불러오기 
import pandas as pd

# k:v 구조를 갖는 딕셔너리를 만들고, 변수 dict_data에 저장
dict_data = {'a': 1, 'b': 2, 'c': 3}

# 판다스 Series() 함수로 딕셔너리(dict_data)를 시리즈로 변환. 변수 sr에 저장 
sr = pd.Series(dict_data)

# 변수 sr의 자료형 출력
print(type(sr))
print('\n')

# 변수 sr에 저장되어 있는 시리즈 객체를 출력
print(sr)
print('\n')

# 인덱스 배열은 변수 idx에 저장. 데이터 값 배열은 변수 val에 저장
idx = sr.index
val = sr.values
print(idx)#Index(['a', 'b', 'c'], dtype='object')
print('\n')
print(val)