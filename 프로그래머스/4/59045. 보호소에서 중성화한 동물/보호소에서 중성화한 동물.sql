# # select ins.animal_id, ins.animal_type, ins.name
# # from animal_ins ins left join animal_outs outs on ins.animal_id = outs.animal_id
# # where ins.SEX_UPON_INTAKE <> outs.SEX_UPON_OUTCOME
# # order by animal_id

# select ins.animal_id, ins.animal_type, ins.name
# from animal_ins ins left join animal_outs outs on ins.animal_id = outs.animal_id
# where ins.SEX_UPON_INTAKE like 'Intact%' and (outs.SEX_UPON_OUTCOME like 'Spayed%' or outs.SEX_UPON_OUTCOME like 'Neutered%')
# order by animal_id

# # -- 코드를 입력하세요
# # SELECT OUTS.ANIMAL_ID, OUTS.ANIMAL_TYPE, OUTS.NAME
# # FROM ANIMAL_OUTS AS OUTS
# # INNER JOIN ANIMAL_INS AS INS
# # ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
# # WHERE OUTS.SEX_UPON_OUTCOME <> INS.SEX_UPON_INTAKE
# # ORDER BY ANIMAL_ID

SELECT O.ANIMAL_ID, O.ANIMAL_TYPE, O.NAME
FROM ANIMAL_OUTS O
INNER JOIN ANIMAL_INS I ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.SEX_UPON_INTAKE != O.SEX_UPON_OUTCOME
ORDER BY O.ANIMAL_ID
