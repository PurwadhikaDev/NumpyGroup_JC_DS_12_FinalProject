use flaskapp;

show tables;

create table CC(
BALANCE decimal(30,2),
BALANCE_FREQUENCY decimal(30,2),
PURCHASES decimal(30,2),
ONEOFF_PURCHASES decimal(30,2),
INSTALLMENTS_PURCHASES decimal(30,2),
CASH_ADVANCE decimal(30,2),
PURCHASES_FREQUENCY decimal(30,2),
ONEOFF_PURCHASES_FREQUENCY decimal(30,2),
PURCHASES_INSTALLMENTS_FREQUENCY decimal(30,2),
CASH_ADVANCE_FREQUENCY decimal(30,2),
CASH_ADVANCE_TRX decimal(30,2),
PURCHASES_TRX decimal(30,2),
CREDIT_LIMIT decimal(30,2),
PAYMENTS decimal(30,2),
MINIMUM_PAYMENTS decimal(30,2),
PRC_FULL_PAYMENT decimal(30,2),
TENURE decimal(30,2),
BALANCE_GROUP char(50),
BALANCE_FREQ_GROUP char(50),
PURCHASES_GROUP char(50),
ONEOFF_PURCHASES_GROUP char(50),
INSTALLMENTS_PURCHASES_GROUP char(50),
CASH_ADVANCE_GROUP char(50),
PURCHASES_FREQ_GROUP char(50),
ONEOFF_PURCHASES_FREQ_GROUP char(50),
PURCHASES_INSTALLMENTS_FREQ_GROUP char(50),
CASH_ADVANCE_FREQ_GROUP char(50),
CASH_ADVANCE_TRX_GROUP char(50),
PURCHASES_TRX_GROUP char(50),
CREDIT_LIMIT_GROUP char(50),
PAYMENTS_GROUP char(50),
MIN_PAYMENTS_GROUP char(50),
PRC_FULL_PAYMENT_GROUP char(50),
SEGMENT decimal(30,2)
);

drop table CC;

SHOW VARIABLES LIKE "secure_file_priv";


LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/CC.csv' 
INTO TABLE CC 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

select * from CC;