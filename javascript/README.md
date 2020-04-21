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