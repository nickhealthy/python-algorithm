SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS I
LEFT OUTER JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL
ORDER BY I.DATETIME
LIMIT 3




# # -- 코드를 입력하세요
# # SELECT INS.NAME, INS.DATETIME
# # FROM ANIMAL_INS AS INS
# # LEFT JOIN ANIMAL_OUTS AS OUTS
# # ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
# # WHERE OUTS.ANIMAL_ID IS NULL
# # ORDER BY INS.DATETIME
# # LIMIT 3

