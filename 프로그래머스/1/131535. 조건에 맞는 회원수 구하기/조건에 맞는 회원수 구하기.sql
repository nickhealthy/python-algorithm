# -- 코드를 입력하세요
# SELECT COUNT(*) AS USERS
# FROM USER_INFO
# WHERE DATE_FORMAT(JOINED, '%Y') = 2021 AND AGE BETWEEN 20 AND 29

SELECT COUNT(*)
FROM USER_INFO
WHERE AGE >= 20 AND AGE <= 29 AND YEAR(JOINED) = 2021
