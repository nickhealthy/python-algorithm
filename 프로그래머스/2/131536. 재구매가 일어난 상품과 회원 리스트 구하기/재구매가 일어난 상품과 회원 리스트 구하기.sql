# -- 코드를 입력하세요
# SELECT USER_ID, PRODUCT_ID, COUNT(*)
# FROM ONLINE_SALE 
# GROUP BY USER_ID, PRODUCT_ID
# HAVING COUNT(*) > 1
# ORDER BY USER_ID, PRODUCT_ID DESC

select user_id, PRODUCT_ID
from online_sale
group by user_id, product_id
having count(*) > 1 
order by user_id asc, PRODUCT_ID desc