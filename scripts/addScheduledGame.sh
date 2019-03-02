#/bin/bash

read -r -d '' q <<EOF


CREATE SEQUENCE id_sequence start 1 increment 1;

INSERT INTO schedule (id, gametime, home, away)
VALUES( nextval('id_sequence'), '2019-02-24 12:30:00', 'Washington Capitals', 'New York Rangers');

EOF

psql -h localhost -d "hockey" -U rich -c "$q"
