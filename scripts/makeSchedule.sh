#/bin/bash

read -r -d '' q <<EOF

DROP SEQUENCE IF EXISTS id_sequence;
DROP TABLE IF EXISTS schedule;

CREATE TABLE schedule (
ID     	     INTEGER    PRIMARY KEY,
GAMETIME     TIMESTAMP,
HOME   	     CHAR(50),
AWAY   	     CHAR(50) 
);

EOF

psql -h localhost -d "hockey" -U rich -c "$q"
