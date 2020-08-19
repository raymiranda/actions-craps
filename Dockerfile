# Container image that runs your code
FROM alpine:3.10

COPY requirements.txt /requirements.txt
# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh

# Copy our dice game to the server.
COPY roll.sh /role.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]