### 1. 완주하지 못한 선수
- 오브젝트 만들고 거기다가 바로 a.'Kiki' = 1이런식으로 집어 넣으려고 하면 undefined오류가 난다   
- a['Kiki'] = 1이런식으로 집어넣으면 들어간다   
- JS에서 object key,value 페어로 출력하려면..   
```javascript
a = {'Kiki':1, 'Amy':2 ...}
for (const [key, value] in Object.entries(a)) {
    console.log(key, value)
}
```

### 2. 모의고사
- array에서 최대값이나 최소값을 구하고 싶을 때 Math 사용
```javascript
const answer = [1,23,100]
const maximum = Math.max(...answer)
const minimum = Math.min(...answer)
```

### 3. 문자열 내 p와 y의 개수
- string의 하나하나 알파벳을 출력하고 싶을 때
```javascript
const myStr = 'answer'
for (const i of myStr) {
    console.log(i)
}
[...myStr].forEach(i => console.log(i))
```