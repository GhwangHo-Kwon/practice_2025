-- 데이터검색 - SELECT
-- 샘플
select employee_id
	 , concat(first_name, ' ', last_name) as 'Name'
     , salary
     , job_id
     , hire_date
     , manager_id
  from employees;

-- 문제1
select concat(first_name, ' ', last_name) as 'Name'
	 , job_id as 'Job'
     , salary as 'Salary'
     , ((salary * 12) + 100) as 'Increased Ann_Salary'
     , ((salary + 100) * 12) as 'Increased Salary'
  from employees;

-- 문제2
select concat(last_name, ': 1 Year Salary = $', (salary * 12)) as '1 Year Salary'
  from employees;

-- 문제3
select distinct department_id, job_id
  from employees;

-- 데이터 제한 및 정렬 - WHERE, ORDER BY
-- 샘플
select concat(first_name, ' ', last_name) as 'Name'
	 , salary
  from employees
 where salary not between 7000 and 10000
 order by salary;

-- 문제1
select last_name as 'e AND o Name'
  from employees
 where last_name like '%e%' and last_name like '%o%';

-- 문제2
select adddate(sysdate(), interval 9 hour) as 'SYSDATE()';

select last_name as 'Name'
	 , employee_id
     , hire_date
  from employees
 where hire_date between '1995-05-20' and '1996-05-20'
 order by hire_date;

-- 문제3