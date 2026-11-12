
import numpy as np

'''
# Numpy - 파이썬에서 수학과 데이터 분석을 쉽게 할 수 있도록 도와주는 라이브러리
# ndArray - 숫자를 여러 차원으로 저장할 수 있는 배열
# Numpy로 할 수 있는 것
    - 숫자 묶음 생성
    - 평균, 합계, 최댓값
    - 배열
    - 2차원 표(행렬)
'''

print("일반 리스트")
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)

print('===== numpy 01 =====')
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
#np.array[] - 리스트처럼 보이지만 수학용 배열, 모든 원소가 같은 타입이어야 한다.
print(a + b)

print('===== numpy 02 =====')
# 1차원 ndArray 생성(숫자4개가 한 줄로 있는 배열)
np.array([1, 2, 3, 4])

arr1 = np.array([1, 2, 3, 4]) #numpy 배열임을 알려줌
arr2 = [1, 2, 3, 4]#일반리스트

#넘파이로 이루어진 다차원 배열
print(type(arr1))

#파이썬 리스트 형태
print(type(arr2))


print('===== numpy 03 =====')
# 1차원 배열 - 숫자가 한 줄로 늘어선 형태
# 2차원 배열 - 숫자가 가로와 세로로 된 표 모양
# 3차원 배열 - 2차원 배열이 여러 장 겹친 입체 모양

# 2차원 ndArray생성
# 1차원 배열 두개가 리스트로 묶인 형태

arr2 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

arr3 = np.array([[[1, 2, 3, 4], [1, 2, 3, 4]],
                [[1, 2, 3, 4], [1, 2, 3, 4]]])

print("2차원 배열")
print(arr2)

print("3차원 배열")
print(arr3)

print('===== numpy 04 =====')

a = np.array([1, 2, 3, 4])
print(a + 1)
print(a * 2)
print(a ** 3)

# for문을 안 쓰고도 계산이 가능하다

print('===== numpy 05 =====')
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])
arr3 = np.array([[[0.1, 0.2, 0.3, 0.4], [5, 6, 7, 8]],
                 [[1, 2, 3, 4], [1, 2, 3, 4]]])

#ndim - 배열의 차원 수
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

#shape - 배열의 형태(배열 구조를 튜플로 보여준다)
#튜풀 - 리스트와 비슷하지만 가장 큰 차이점은 한 번 생성한 튜플의 요소를 수정하거나 삭제할 수 없다.
# (총개수, 행개수, 열개수)
print(arr1.shape) # (4, )
print(arr2.shape) # (2, 4) = 8개
print(arr3.shape) # (2, 2, 4) = 16개

# size - 배열 요소의 총 개수
print(arr1.size) # 4
print(arr2.size) # 8
print(arr3.size) # 16

# dtype - 배열 요소의 데이터 타입
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)

# itemsize - 배열 원소 하나가 차지하는 메모리 크기(byte 기준)
print(arr1.itemsize)
print(arr2.itemsize)
print(arr3.itemsize)

#data - 배열으 ㅣ실제 데이터가 저장된 메모리 버퍼(buffer 주소)
print(arr1.data)
print(arr2.data)
print(arr3.data)


print('===== numpy 06 =====')
#ndArray T - 전치 행렬(행/열을 서로 바꾸는 것)
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("원래 행렬")
print(arr)

print("전치 행렬")
print(arr.T)


print('===== numpy 06 =====')
#ndArray.flatten() - 1차원으로 펼치기

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("원래 배렬")
print(arr)

print("1차원로 펼친 배렬")
print(arr.flatten())

# flatten()은 복사본(copy)를 만든다
flat =arr.flatten()
flat[0] = 100

print("배열 출력")
print(flat)