use Hotel;

INSERT INTO customer (name, email, phone, is_vip, loyalty_points)
VALUES 
    ('Jan Novák',       'jan.novak@example.com',       '+420123456789', TRUE,  150.00),
    ('Petr Svoboda',    'petr.svoboda@example.com',    '+420987654321', FALSE,  50.00),
    ('Lucie Dvořáková', 'lucie.dvorakova@example.com', '+420606606606', FALSE, 120.00),
    ('Kateřina Malá',   'katerina.mala@example.com',   '+420777888999', TRUE,   80.00),
    ('Tomáš Novotný',   'tomas.novotny@example.com',   '+420724123456', FALSE,  0.00);



INSERT INTO points_history (customer_id, ammount, description)
VALUES
    (1, 50.00, 'Vstupní bonus'),
    (1, 100.00, 'Propagační akce'),
    (2, 50.00, 'Doporučení nového klienta'),
    (3, 20.00, 'Pravidelné využívání služeb'),
    (3, 100.00, 'Promo kampaň'),
    (4, 30.00, 'Věrnostní bonus'),
    (4, 50.00, 'Black Friday bonus'),
    (5, 10.00, 'Základní uvítací bonus');



INSERT INTO room (room_number, capacity, price_per_night, room_type)
VALUES
    ('101', 2,  1200.00, 'STANDARD'),
    ('102', 2,  1400.00, 'DELUXE'),
    ('201', 3,  1600.00, 'DELUXE'),
    ('202', 4,  2500.00, 'SUITE'),
    ('301', 1,   900.00, 'STANDARD');



INSERT INTO reservation (customer_id, reservation_date, check_in, check_out)
VALUES
    (1, '2025-01-10 14:00:00', '2025-02-01', '2025-02-05'),
    (2, '2025-01-12 10:30:00', '2025-03-15', '2025-03-18'),
    (3, '2025-01-15 09:20:00', '2025-04-10', '2025-04-12'),
    (4, '2025-01-20 16:45:00', '2025-05-01', '2025-05-03'),
    (5, '2025-01-25 11:05:00', '2025-06-10', '2025-06-15');
    
    
    
INSERT INTO reservation_room (reservation_id, room_id, price_applied)
VALUES
    (1, 1, 1200.00), -- Rezervace 1, pokoj 101 (STANDARD)
    (1, 2, 1400.00), -- Rezervace 1, pokoj 102 (DELUXE)
    (2, 3, 1600.00), -- Rezervace 2, pokoj 201 (DELUXE)
    (3, 4, 2500.00), -- Rezervace 3, pokoj 202 (SUITE)
    (4, 1, 1200.00), -- Rezervace 4, pokoj 101 (STANDARD)
    (5, 2, 1400.00), -- Rezervace 5, pokoj 102 (DELUXE)
    (5, 3, 1600.00); -- Rezervace 5, pokoj 201 (DELUXE)
    
    
    
    INSERT INTO payment (reservation_id, payment_date, amount, method)
VALUES
    (1, '2025-02-05 12:00:00', 2600.00, 'CARD'),
    (2, '2025-03-18 09:00:00', 1600.00, 'CASH'),
    (3, '2025-04-12 18:30:00', 2500.00, 'BANK_TRANSFER'),
    (4, '2025-05-03 08:15:00', 1200.00, 'CARD'),
    (5, '2025-06-15 14:10:00', 3000.00, 'CASH');

