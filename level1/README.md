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
# 몫과 나머지를 반환한다
```

### 1-9
- 같은 숫자는 싫어
```python
a = []
print(a[-1:])
# a[-1]을 하면 빈 배열이기 때문에 오류가 나지만 a[-1:]로 부르면 그냥 빈배열이 나온다
```

### 1-10
- 나누어떨어지는 숫자배열    
- if else로 return하는 부분을 한줄로 줄여서 많이 쓴다   

### 1-11
- 문제 이해를 잘못했다   
- n번째 인덱스 기준으로 정렬하고 같으면 사전순 정렬 ([n:]부터 사전 정렬인줄 착각했다)   
- 전체 sort해준 다음 [n] 기준으로 sort 해주면된다   

### 1-12
- H-index   
- 문제 이해를 잘 못했음..   
```python
case = [100,100,100,100] 
# 이 경우 h-index는 4가 되어야 하는데 아무것도 출력을 안하는 코드를 짬
# 현재 index와 case[index] 중 최소값 -> 최소값과 answer 중 최대값을 출력하면 된다
```

### 1-13
- 약수의 합   
- 처음에 그냥 n까지 약수 하나하나 구함(최대 n이 3000으로 작았기 때문)   
- 두번째 다른 사람 풀이 보고 n//2+1번째 수까지 약수 구한 후 n에 더하는 방법 알게됨   
- n이 계속 갱신되는 방법으로 짜서 틀림 -> 리스트 안에 넣고 n에 sum(list) 더함   