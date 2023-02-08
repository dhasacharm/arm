FROM postgres:9.6.21
ENV POSTGRES_PASSWORD=ahmedpostgres
EXPOSE 5432
COPY init.db.sh /tmp/