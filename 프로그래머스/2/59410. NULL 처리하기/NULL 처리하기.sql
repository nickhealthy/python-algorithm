# select animal_type, ifnull(name, 'No name') as name, sex_upon_intake
# from animal_ins

# -- 코드를 입력하세요
# SELECT ANIMAL_TYPE, IFNULL(NAME, "No name") AS NAME, SEX_UPON_INTAKE
# FROM ANIMAL_INS

SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE
FROM ANIMAL_INS
