CREATE TABLE job(
	id int NOT NULL PRIMARY KEY,
	basicdesc NOT NULL,
	fulldesc NOT NULL,
	location NOT NULL
)

CREATE TABLE INFO(
	nameid int NOT NULL PRIMARY KEY,
	name NOT NULL,
	source NOT NULL,
	experience NOT NULL,
	summary NOT NULL
)