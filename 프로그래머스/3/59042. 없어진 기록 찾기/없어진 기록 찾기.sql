# select outs.animal_id, outs.name
# from animal_outs outs
# left outer join animal_ins ins
# on outs.animal_id = ins.animal_id
# where ins.animal_id is null
# order by outs.animal_id, outs.name



# # SELECT OUTS.ANIMAL_ID, OUTS.NAME
# # FROM ANIMAL_OUTS AS OUTS
# # LEFT OUTER JOIN ANIMAL_INS AS INS
# # ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
# # WHERE INS.ANIMAL_ID IS NULL
# # ORDER BY ANIMAL_ID

SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS OUTS
LEFT OUTER JOIN ANIMAL_INS INS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.ANIMAL_ID IS NULL
ORDER BY ANIMAL_ID