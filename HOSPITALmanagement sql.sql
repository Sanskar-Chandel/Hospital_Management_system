use hospital_management;
select * from hospital;







CREATE TABLE hospital (
    Nameoftablets INT NOT NULL,
    `Reference No` VARCHAR(45) NOT NULL,
    dose VARCHAR(45) NULL,
    Numbersoftablets VARCHAR(45) NULL,
    lot VARCHAR(45) NULL,
    issuedate VARCHAR(45) NULL,
    expdate VARCHAR(45) NULL,
    dailydose VARCHAR(45) NULL,
    storage VARCHAR(45) NULL,
    nhsnumber VARCHAR(45) NULL,
    patientname VARCHAR(45) NULL,
    DOB VARCHAR(45) NULL,
    patientaddress VARCHAR(45) NULL,
    PRIMARY KEY (`Reference No`)
);





SELECT* FROM hospital;