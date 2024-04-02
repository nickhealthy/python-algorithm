# -- 코드를 입력하세요
# SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
# FROM MEMBER_PROFILE
# WHERE GENDER = 'W' AND MONTH(DATE_OF_BIRTH) = 3 AND NOT TLNO IS NULL
# ORDER BY MEMBER_ID;

select member_id, member_name, gender, date_format(date_of_birth, '%Y-%m-%d') as date_of_birth
from member_profile
where gender = 'W' and not tlno is null and month(date_of_birth) = 3
order by member_id;