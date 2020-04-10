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