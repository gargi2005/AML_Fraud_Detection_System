-- View All Transactions
SELECT * FROM transactions;


-- Fraud Transactions
SELECT *
FROM transactions
WHERE is_fraud = 1;


-- High Value Transactions
SELECT *
FROM transactions
WHERE TransactionAmount > 100000;


-- Average Transaction Amount
SELECT AVG(TransactionAmount)
FROM transactions;


-- Top 10 Highest Transactions
SELECT *
FROM transactions
ORDER BY TransactionAmount DESC
LIMIT 10;


-- Transactions By Day
SELECT day_of_week, COUNT(*) AS total_transactions
FROM transactions
GROUP BY day_of_week;


-- Suspicious Accounts
SELECT AccountId, COUNT(*) AS fraud_count
FROM transactions
WHERE is_fraud = 1
GROUP BY AccountId
ORDER BY fraud_count DESC;


-- High Risk Transactions
SELECT *
FROM transactions
WHERE RiskCategoryId = 3;


-- Low Balance High Transaction
SELECT *
FROM transactions
WHERE Balance < 10000
AND TransactionAmount > 50000;


-- Night Transactions
SELECT *
FROM transactions
WHERE transaction_hour >= 23
OR transaction_hour <= 4;