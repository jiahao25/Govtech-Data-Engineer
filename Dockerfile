#pull base image
FROM postgres
MAINTAINER jiahao

#set environmental variables
ENV POSTGRES_PASSWORD postgres

# copy sql file. the sql file will be run when the container runs.
COPY carDealership.sql /docker-entrypoint-initdb.d/