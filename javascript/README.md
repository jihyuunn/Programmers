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

### 4. 가운데 글자 가져오기
- string을 자를 때 slice함수를 써야한다   
- 하지만 단 하나의 문자를 가져올 때는 someString[n]도 가능하다   

### 5. 문자열 다루기 기본
- string안에 어떤 substring이 포함되어있는지 알고싶을 때
```javascript
const string = 'abcde';
const subString = 'a';
string.includes(subString);
// true 혹은 false가 리턴된다
```

### 6. 위장   
- object안에는 무조건 key,value쌍으로 들어가야한다   
- object안에서 해당 키값이 있는지 확인 할 수 있는 내장 객체
```javascript
const myObject = {first: 0, second: 2}
console.log(myObject.hasOwnProperty('first')) // true
console.log(myObject.hasOwnProperty(2)) // false

for (let i in myObject) {
    console.log(i)
}
// first
// second
```
