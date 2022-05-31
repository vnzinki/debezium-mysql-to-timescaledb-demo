FROM confluentinc/cp-kafka-connect-base:6.2.4
# FROM bitnami/kafka:2.5.0
RUN confluent-hub install --no-prompt debezium/debezium-connector-mysql:latest &&\
    confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:latest
