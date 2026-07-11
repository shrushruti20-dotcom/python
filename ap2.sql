CREATE TABLE OBJ (
    SNO TEXT PRIMARY KEY,
    STATE TEXT,
    CAPITAL TEXT
    
);

INSERT INTO OBJ (SNO, STATE, CAPITAL) VALUES
('1', 'Tamil Nadu','CHENNAI'),
('2', 'Karnataka', 'BENGALURU'),
('3', 'Kerala','TRIVANANTHAPURAM'),
('4', 'Goa','PANGI' ),
('5', 'Andra pradesh','AMARAVATHI' );

SELECT * FROM OBJ;