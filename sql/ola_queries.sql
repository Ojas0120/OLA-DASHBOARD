-- Q1 Total rides
SELECT COUNT(*) AS total_rides
FROM ola_rides;

-- Q2 Ride status distribution
SELECT ride_status, COUNT(*) AS total
FROM ola_rides
GROUP BY ride_status;

-- Q3 Cancellation percentage
SELECT
    ROUND(
            (COUNT(CASE WHEN ride_status='Cancelled' THEN 1 END) * 100.0)
                / COUNT(*), 2
    ) AS cancellation_rate
FROM ola_rides;

-- Q4 Total revenue
SELECT SUM(fare) AS total_revenue
FROM ola_rides
WHERE ride_status='Completed';

-- Q5 Revenue by payment mode
SELECT payment_mode, SUM(fare) AS revenue
FROM ola_rides
WHERE ride_status='Completed'
GROUP BY payment_mode;

-- Q6 Peak ride hours
SELECT hour, COUNT(*) AS rides
FROM ola_rides
GROUP BY hour
ORDER BY rides DESC;

-- Q7 Top pickup locations
SELECT pickup_location, COUNT(*) AS rides
FROM ola_rides
GROUP BY pickup_location
ORDER BY rides DESC
    LIMIT 5;

-- Q8 Average fare
SELECT ROUND(AVG(fare),2) AS avg_fare
FROM ola_rides
WHERE ride_status='Completed';

-- Q9 Top drivers
SELECT driver_id, COUNT(*) AS rides
FROM ola_rides
GROUP BY driver_id
ORDER BY rides DESC
    LIMIT 5;

-- Q10 Average customer rating
SELECT ROUND(AVG(customer_rating),2) AS avg_rating
FROM ola_rides;
