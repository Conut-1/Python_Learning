SELECT DISTINCT CAR_RENTAL_COMPANY_RENTAL_HISTORY.CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY JOIN CAR_RENTAL_COMPANY_CAR ON CAR_RENTAL_COMPANY_RENTAL_HISTORY.CAR_ID = CAR_RENTAL_COMPANY_CAR.CAR_ID
WHERE MONTH(START_DATE) = 10 AND CAR_TYPE = '세단'
ORDER BY CAR_ID DESC;
