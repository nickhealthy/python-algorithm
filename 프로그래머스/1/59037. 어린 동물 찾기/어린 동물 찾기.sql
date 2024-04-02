# select animal_id, name from animal_ins
# where intake_condition <> 'Aged'
# order by animal_id

# SELECT ANIMAL_ID, NAME
# FROM ANIMAL_INS
# WHERE INTAKE_CONDITION <> 'Aged'
# ORDER BY ANIMAL_ID

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
ORDER BY ANIMAL_ID
