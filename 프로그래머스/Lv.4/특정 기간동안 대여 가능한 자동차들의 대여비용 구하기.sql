SELECT C.CAR_ID, C.CAR_TYPE, FLOOR(DAILY_FEE * 30 * (100 - DISCOUNT_RATE) / 100) AS FEE
FROM CAR_RENTAL_COMPANY_CAR AS C
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS D ON C.CAR_TYPE = D.CAR_TYPE
WHERE C.CAR_TYPE IN ('세단', 'SUV') 
    AND D.DURATION_TYPE = '30일 이상'
    AND C.CAR_ID NOT IN (
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE START_DATE <= '2022-11-30'
        AND END_DATE >= '2022-11-01'
    )
GROUP BY C.CAR_ID
HAVING FEE >= 500000 AND FEE < 2000000
ORDER BY FEE DESC, C.CAR_TYPE, C.CAR_ID DESC;
