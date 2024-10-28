-- 0 list privileges of user 1 and 2
SELECT * FROM information_schema.user_privileges
WHERE grantee LIKE "'user_0d_1'@'localhost'";

SELECT * FROM information_schema.user_privileges
WHERE grantee LIKE "'user_0d_2'@'localhost'";