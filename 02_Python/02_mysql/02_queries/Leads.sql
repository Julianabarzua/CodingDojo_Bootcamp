SELECT date_format(charged_datetime,"%M") as month, sum(amount)
FROM lead_gen_business.billing
WHERE  date_format(charged_datetime,"%M") = "March" AND date_format(charged_datetime,"%Y") = 2012;

SELECT client_id, sum(amount)
FROM lead_gen_business.billing
WHERE client_id =2;

SELECT domain_name, client_id
FROM sites
WHERE client_id =10;

SELECT count(domain_name), client_id, date_format(created_datetime,"%M") as month, date_format(created_datetime,"%Y") as year
FROM sites
WHERE client_id =1
GROUP BY date_format(created_datetime,"%M"), date_format(created_datetime,"%Y");

SELECT count(domain_name), client_id, date_format(created_datetime,"%M") as month, date_format(created_datetime,"%Y") as year
FROM sites
WHERE client_id =20
GROUP BY date_format(created_datetime,"%M"), date_format(created_datetime,"%Y");

SELECT concat(c.first_name," ", c.last_name), count(leads_id)
FROM sites as s
JOIN leads as l on s.site_id = l.site_id
JOIN clients as c on c.client_id = s.client_id
WHERE registered_datetime >= "2011/01/01" AND registered_datetime <= "2011/12/31"
GROUP BY concat(c.first_name," ", c.last_name);

SELECT concat(c.first_name," ", c.last_name), count(leads_id), date_format(registered_datetime, "%M")
FROM sites as s
JOIN leads as l on s.site_id = l.site_id
JOIN clients as c on c.client_id = s.client_id
WHERE registered_datetime >= "2011/01/01" AND registered_datetime <= "2011/06/30"
GROUP BY date_format(registered_datetime, "%M"),concat(c.first_name," ", c.last_name) ;

SELECT concat(c.first_name," ", c.last_name), domain_name, count(leads_id)
FROM sites as s
JOIN leads as l on s.site_id = l.site_id
JOIN clients as c on c.client_id = s.client_id
GROUP BY concat(c.first_name," ", c.last_name), domain_name 
order by c.client_id, domain_name; 

SELECT concat(c.first_name," ", c.last_name) as client_name, sum(amount) as total_revenue, date_format(charged_datetime,"%M"),date_format(charged_datetime,"%Y")
FROM clients as c
JOIN billing as b on c.client_id = b.client_id
ORDER BY c.client_id,date_format(charged_datetime,"%M"),date_format(charged_datetime,"%Y");

SELECT concat(c.first_name," ", c.last_name) as client_name, sum(amount) as total_revenue, date_format(charged_datetime,"%M"),date_format(charged_datetime,"%Y")
FROM clients as c
JOIN billing as b on c.client_id = b.client_id
GROUP BY c.client_id, date_format(charged_datetime,"%M"),date_format(charged_datetime,"%Y")
order by c.client_id,date_format(charged_datetime,"%Y"), date_format(charged_datetime,"%M") ;

SELECT concat(first_name, " ", last_name), group_concat(domain_name)
FROM clients as c
JOIN sites as s ON c.client_id = s.client_id
GROUP BY concat(first_name, " ", last_name)
ORDER BY c.client_id;


