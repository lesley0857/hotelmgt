#!/bin/sh
# until cd /app/
# do
#     echo "Waiting for server volume..."
# done

# run a worker 
celery --app=hotelmgtproj worker --pool=solo -l INFO
celery -A hotelmgtproj beat -l INFO