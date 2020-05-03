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

### 7. 문자열을 정수로 바꾸기
- parseInt는 string의 시작부터 숫자가 나오는 부분을 그냥 숫자로 바꿔준다   
```javascript
const a = '1234qwer';
parseInt(a);
// 1234
Number(a);
// Nan
parseInt(string, radix);
// sting을 radix에 써져있는 진수에서 10진수로 바꿔준다.
```

### 8. K번째수
- js에도 array.sort() 함수가 있지만 string기준으로 sort한다   
- sort()안에 compare 함수를 넣어줘야 숫자 기준으로 sort가 된다   
```javascript
const someArray = [2, 1, 20, 100, 300]
someArray.sort()
// [1, 100, 2, 200, 300]
someArray.sort(function(a, b) {return a - b})
// [1, 2, 100, 200, 300]
```

### 9. 기능개발
- python처럼 초기 배열 크기 선언할 때 곱하기로는 안된다   
- 다양한 테스트케이스 만들어봐야함   
```javascript
const a = Array(6).fill(0);
// [0,0,0,0,0,0]
``` 

### 10. 가장 큰 수
- javascript의 sort함수에 대한 이해가 부족하다   
```javascript
const a = [
    {name: 'a', age: 2},
    {name: 'b', age: 30},
    {name: 'c', age: 23},
    {name: 'd', age: 6},
]
a.sort((a,b) => b.name>a.name?1:a.name>b.name?-1:0);
// d,c,b,a
a.sort((a,b) => b.age - a.age);
// 30,23,6,2
```

### 11. 124나라의 숫자   
- 숫자를 더하는 위치 조심하기   
```javascript
const s = "abcde";
console.log(s.split("").reverse().join(""));
// edcba
```

### 12. 탑   
- javascript의 reverse()함수는 array를 뒤집는 함수이기 때문에 124나라의 숫자처럼 string을 뒤집어주기 위해서는 split()함수로 array로 바꿔준 후에 reverse할 수 있다   
- map함수에서 현재 value와 index를 한번에 가져올 수 있고, map함수는 원래 array를 바꾸는게 아니라 새로운 array를 반환한다   
```javascript
const a = [1,2,3,4,5];
a.map((currentValue, index) => {
    while (i) {
        i--;
        // 여기서 앞의 인덱스 숫자가 더 큰게 있는지 확인 가능
    }
})
```

### 13. 프린터    
- break loop이 안되는 것 같다   

### 14. 큰 수 만들기
- slice는 원래 배열을 바꾸지 않고 splice는 원래 배열을 바꾼다   
- indexOf    
- 가장 큰수인 9를 찾았을 때 break를 해주면 시간이 훨씬 줄어든다   