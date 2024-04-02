# -- 코드를 입력하세요
# SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD
# FROM DOCTOR
# WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
# ORDER BY HIRE_YMD DESC, DR_NAME

select DR_NAME, dr_id, mcdp_cd, date_format(hire_ymd, '%Y-%m-%d') as hire_ymd
from doctor
where mcdp_cd = 'CS' or mcdp_cd = 'GS'
order by hire_ymd desc, dr_name asc 