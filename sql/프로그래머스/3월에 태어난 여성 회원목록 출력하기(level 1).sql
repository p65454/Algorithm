# https://school.programmers.co.kr/learn/courses/30/lessons/131120
# 날짜 date format 활용
SELECT MEMBER_ID
     , MEMBER_NAME
     , GENDER     
     , DATE_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d') AS DATE_OF_BIRTH
 FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH) = '3' AND GENDER = 'W' AND NOT TLNO IS NULL
ORDER BY MEMBER_ID ASC
;