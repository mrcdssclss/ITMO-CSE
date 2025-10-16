CREATE TABLE material( 	id SERIAL PRIMARY KEY, 	material_name TEXT NOT NULL
);

CREATE TABLE floor( 	id SERIAL PRIMARY KEY,
	test TEXT NOT NULL, 	id_material SERIAL REFERENCES material(id)
);
 CREATE TABLE IF NOT EXISTS ceiling( id SERIAL PRIMARY KEY, id_material SERIAL REFERENCES material(id));

CREATE TABLE IF NOT EXISTS tomb( id SERIAL PRIMARY KEY,
id_floor SERIAL REFERENCES floor(id),
id_ceiling SERIAL REFERENCES ceiling(id), tomb_name TEXT NOT NULL);

CREATE TABLE IF NOT EXISTS tomb_material( id_tomb SERIAL REFERENCES tomb(id), id_material SERIAL REFERENCES material(id));
 INSERT INTO tomb(id_floor, id_ceiling, tomb_name) VALUES (1, 1, 'Усыпальница Ярлана Зея');
 INSERT INTO ceiling(id_material) VALUES (1);
 INSERT INTO floor(id_material) VALUES (1);
 INSERT INTO tomb_material(id_tomb, id_material) VALUES (1, 1);
 INSERT INTO material(material_name) VALUES ('Камень');
