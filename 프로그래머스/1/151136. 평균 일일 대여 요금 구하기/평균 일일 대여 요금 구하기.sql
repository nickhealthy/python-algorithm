# -- 코드를 입력하세요
# SELECT ROUND(AVG(DAILY_FEE)) AS AVERAGE_FEE
# FROM CAR_RENTAL_COMPANY_CAR
# WHERE CAR_TYPE = 'SUV'

select round(avg(daily_fee)) as average_fee
from CAR_RENTAL_COMPANY_CAR
where car_type = 'SUV'
