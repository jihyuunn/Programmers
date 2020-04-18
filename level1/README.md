### 1-3
- 완주하지 못한 선수    
- 딕셔너리를 사용했지만, python의 counter함수를 쓰면 더 쉽게 풀이 가능하다   
```python
import collections
answer = collections.Counter(participant)-collections.Counter(completion)
# 딕셔너리의 형태로 반환된다. 그런데 딕셔너리는 빼기가 불가능하지만 Counter객체이기때문에 빼기 가능하다 
```

### 1-4
- 모의고사   
- 푸는 방법은 programmers에서 가장 위에있는 풀이와 똑같다   
- 다만 마지막에 정답 출력하는 부분에서 enumerate함수를 쓰면 더 발전 가능하다   
```python
for index, score in enumerate(answer):
    if i == max(answer):
        ans.append(i+1)
```

### 1-5
- 체육복   
- O(n)   
- lambda를 사용하면 한줄로 해결 가능   
- lambda, reduce, filter 함수 공부   

### 1-7
- 2016년   
- 잘 푼것 같다   

### 1-8
- 124 나라의 숫자   
- python divmod()함수를 많이 쓴다   
```python
q,r = divmod(n-1, 3)
```