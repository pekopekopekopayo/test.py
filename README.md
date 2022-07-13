# Django 테스트 공간

## 1. test1 역참조 vs filter filter
- filter가 조금 더 빠르다.
## 2. pre_fetch vs filter
- 서버속도, DB속도 filter가 조금 더 빠르다. 

## 3. with vs sub 
- with은 가상테이블을 만든후 활용할때 사용함으로 범용성있게 사용 할 수 있지만 sub에 비해 느림 간단한 문장에서는 sub가 조금 더 빠름
- 활용하기 나름인듯하다.