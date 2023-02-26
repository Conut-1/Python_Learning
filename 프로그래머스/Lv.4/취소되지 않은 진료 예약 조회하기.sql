SELECT APNT_NO, PT_NAME, P.PT_NO, D.MCDP_CD, DR_NAME, APNT_YMD
FROM APPOINTMENT AS A
    JOIN PATIENT AS P ON A.PT_NO = P.PT_NO
    JOIN DOCTOR AS D ON A.MDDR_ID = D.DR_ID
WHERE APNT_CNCL_YN = 'N'
    AND DATE_FORMAT(APNT_YMD, '%Y-%m-%d') = '2022-04-13'
    AND D.MCDP_CD = 'CS'
ORDER BY APNT_YMD;
