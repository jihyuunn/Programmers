### 2-a
- left, right로 인덱싱 조절 
- current에 현재 index의 다음 인덱스를 더한 단어가 dictionary에 있는지 확인   
1. 있으면 다음 index까지 포함한 단어의 숫자를 answer에 append   
2. 없으면 다음 index까지 포함한 단어를 새로 dictionary에 넣고 현재 index까지 단어의 숫자를 answer에 append   
- 마지막 문자를 포함한 단어가 dictionary에 있는지 없는지 구분하여 넣어주기   

### 2-b
- 처음에 이름이 스킬트리여서 트리를 쓰는건가... 삽질   
- check 배열로 만들어서 이전 스킬을 다 배웠는지 확인하려함 -> for문 3중으로 돌려야됨   
- check배열없이 현재 몇번째 skill을 배워야하는지 index만 기억하고 있으면 된다   
1. 현재 스킽트리에서 skill에 포함된 글자가 나오면 index보다 작거나 같아야한다
2. index보다 크면 이전 스킬을 안배웠다는 의미이므로 check=False로 기록   
3. check=True인 경우만 answer += 1   

### 2-c   
- 크게 어렵지 않은 문제였는데 내가 생각 못한 예외 케이스가 있었다 -> 테스트케이스 중요...   
- 첫번째 글자면 uppercase로 하고 first = False로 만들어주고 그 외에 글자면 lowercase로 하고 공백일 시에 first = True로 만들어주기   
- 그런데 중간에 공백이 여러개 있을 때 첫번째 공백에서 True -> 두번째 공백에서 False 가 되어서 세번째에 글자가 나오면 제대로 uppercase로 못바꿔 주었다   
-> 아예 if else끝나고 마지막에 공백인지 체크하고 공백이면 True로 바꿔줌

### 2-d
- 복잡한 문제지만 설명이 순서대로 잘 되어있어서 그대로 코딩하면 된다   
- 사실 전에 한번 풀어본 문제..   

### 2-e
- 프린트 큐 문제   
- 큐 배열에 아무것도 없을 때를 생각해야된다   
```python
queue = [(i,p) for i,p in enumerate(priorities)]
if any(current[1] < q[1] for q in queue)
```
1. enumerate 함수는 인덱스값, 밸류를 리턴하는 함수이다   
2. any 함수는 전달 받은 자료형의 element중 하나라도 True일 경우 True를 리턴한다   

### 2-f
- 가장 큰 수    
- 처음에 그냥 조합으로 풀려고 했음 O(len(numbers)!) => 바로 시간초과남   
- 그래서 큰 수를 먼저 넣어주고 앞자리 숫자가 같은애들만 다시 sort => 시간초과   
- 그냥 정렬을 해주면 되는게 아니고 각 원소들을 string으로 바꿔준 후에 *3을 하면 된다   
-> 그러면 string이기 때문에 각 숫자를 더해야되는 순서대로 sort 가능   

