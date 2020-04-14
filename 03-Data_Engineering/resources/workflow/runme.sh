hdfs dfs -put workflow/
export OOZIE_URL="https://nightly63x-1.nightly63x.root.hwx.site:11443/oozie"
# export OOZIE_URL="http://nightly63x-1.nightly63x.root.hwx.site:11000/oozie"
# export OOZIE_CLIENT_OPTS="-Djavax.net.ssl.trustStore=/etc/cdep-ssl-conf/CA_STANDARD/truststore.jks"
oozie job -config shell.properties -run
