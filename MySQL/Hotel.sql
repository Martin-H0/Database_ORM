USE Hotel;
-- SET AUTOCOMMIT = OFF;
-- START transaction;

CREATE TABLE customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(30),
    is_vip BOOLEAN DEFAULT FALSE,
    loyalty_points FLOAT DEFAULT 0 NOT NULL
);
CREATE TABLE points_history(
	id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    ammount decimal(10,2),
    description varchar(50),
    CONSTRAINT fk_points_history_customer
        FOREIGN KEY (customer_id) REFERENCES customer(id)    
);

CREATE TABLE room (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(10) NOT NULL,
    capacity INT NOT NULL,
    price_per_night FLOAT NOT NULL,
    room_type ENUM('STANDARD','DELUXE','SUITE') NOT NULL
);

CREATE TABLE reservation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    reservcustomercustomeration_date DATETIME default(current_time()) NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,
    CONSTRAINT fk_reservation_customer
        FOREIGN KEY (customer_id) REFERENCES customer(id)
);

CREATE TABLE payment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reservation_id INT NOT NULL, -- UNIQUE PRO 11
    payment_date DATETIME default(current_time()) NOT NULL,
    amount FLOAT NOT NULL,
    method VARCHAR(30) CHECK(method IN ('CARD','CASH','BANK_TRANSFER')) NOT NULL,
    CONSTRAINT fk_payment_reservation
        FOREIGN KEY (reservation_id) REFERENCES reservation(id)
);

CREATE TABLE reservation_room (
	id INT AUTO_INCREMENT PRIMARY KEY,
    reservation_id INT NOT NULL,
    room_id INT NOT NULL,
    price_applied FLOAT NOT NULL,
    CONSTRAINT fk_resroom_reservation
        FOREIGN KEY (reservation_id) REFERENCES reservation(id),
    CONSTRAINT fk_resroom_room
        FOREIGN KEY (room_id) REFERENCES room(id)
);


DELIMITER **
CREATE VIEW view_customer_points AS
SELECT 
    c.id AS customer_id,
    c.name AS customer_name,
    c.email,
    c.loyalty_points AS current_loyalty_points,
    IFNULL(SUM(ph.ammount), 0) AS total_points_earned,
    COUNT(DISTINCT r.id) AS total_reservations
FROM customer c
    LEFT JOIN points_history ph ON ph.customer_id = c.id
    LEFT JOIN reservation r ON r.customer_id = c.id
GROUP BY 
    c.id, c.name, c.email, c.loyalty_points;
**

DELIMITER **
CREATE VIEW view_reservation_details AS
SELECT 
    r.id AS reservation_id,
    c.name AS customer_name,
    r.check_in,
    r.check_out,
    ro.room_number,
    ro.room_type,
    rr.price_applied
FROM reservation r
    JOIN customer c ON r.customer_id = c.id
    JOIN reservation_room rr ON rr.reservation_id = r.id
    JOIN room ro ON rr.room_id = ro.id;
**

DELIMITER **
CREATE VIEW view_invoice_summary AS
SELECT
    p.id AS payment_id,
    c.name AS customer_name,
    r.check_in,
    r.check_out,
    p.amount AS payment_amount,
    p.payment_date,
    p.method AS payment_method
FROM payment p
    JOIN reservation r ON p.reservation_id = r.id
    JOIN customer c ON r.customer_id = c.id;
**

DELIMITER //
CREATE PROCEDURE proc_transfer_points(IN _from_id int,IN _to_id int,IN _ammount int)
BEGIN
    UPDATE customer 
    SET loyalty_points = loyalty_points-_ammount WHERE id = _from_id;
    
    insert into points_history(customer_id,ammount,description) values(_from_id,-_ammount,'Převod');
    
    UPDATE customer 
    SET loyalty_points = loyalty_points+_ammount WHERE id = _to_id;
    
    insert into points_history(customer_id,ammount,description) values(_to_id,_ammount,'Převod');
END //


