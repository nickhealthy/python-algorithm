# -- 코드를 입력하세요
# SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO
# FROM PATIENT
# WHERE AGE <= 12 AND GEND_CD = 'W'
# ORDER BY AGE DESC, PT_NAME

select pt_name, pt_no, gend_cd, age, ifnull(tlno, 'NONE') as TLNO
from patient
where age <= 12 and gend_cd = 'W'
order by age desc, pt_name asc