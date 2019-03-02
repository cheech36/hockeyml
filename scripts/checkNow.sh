#/bin/bash

read -r -d '' q <<EOF

SELECT NOW();

EOF

psql -h localhost -d "hockey" -U rich -c "$q"
