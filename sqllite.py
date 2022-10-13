CREATE TABLE EMPLOYEE(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL0);



CREATE TABLE DEPARTMENT(
   ID INT PRIMARY KEY      NOT NULL,
   DEPT           CHAR(50) NOT NULL,
   EMP_ID         INT      NOT NULL
);




CREATE TABLE PROJECT(
   ID INT PRIMARY KEY      NOT NULL,
   NAME           CHAR(50) NOT NULL,
);


CREATE TABLE project_assignees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emp_id INTEGER,
    project_id INTEGER,
    FOREIGN KEY(emp_id) REFERENCES items(id),
    FOREIGN KEY(project_id) REFERENCES assignees(id)
);
