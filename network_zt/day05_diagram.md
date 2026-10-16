# day05 경보 판단

## 이상한 줄
- 줄 번호(여러 개면 모두): 
  
2  03:12  192.0.2.7    → DB  3306   permit
3  03:13  192.0.2.7    → DB  3306   permit

- 이유: INTERNET → DB 접속 허용되면 안됨.

## 고친 구성도
```
INTERNET ─── FW ──┬── DMZ    (WEB : 443 허용)
                  └── INSIDE (DB  : 3306은 WEB에서만 허용)

차단 규칙: INTERNET → DB (3306)
```
