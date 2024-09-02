-- CREATE TABLE Employee (
--     Name varchar(255),
--     Position varchar(255),
--     Department varchar(255),
--     Salary int
-- );

-- INSERT INTO Employee (Name, Position, Department, Salary)
-- VALUES ("Kirill", "Developer", "IT", 8000),
--        ("Artem", "Deliveryman", "Sales", 1000),
--        ("Ivan", "Designer", "Sales", 6000);

-- UPDATE Employee set Position = "Manager" WHERE Name = "Artem";

-- ALTER TABLE Employee ADD HireDate DATE;

-- UPDATE Employee set HireDate = "2023-08-15" WHERE Name = "Kirill";
-- UPDATE Employee set HireDate = "2022-06-20" WHERE Name = "Artem";
-- UPDATE Employee set HireDate = "2024-03-13" WHERE Name = "Ivan";

-- SELECT * FROM Employee WHERE Position = "Manager";

-- SELECT * FROM Employee WHERE Salary > 5000;

-- SELECT * FROM Employee WHERE Department = "Sales";

-- SELECT AVG(Salary) FROM Employee;

-- DROP TABLE Employee;