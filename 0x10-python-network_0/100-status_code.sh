#!/bin/bash
# displays only the status code of the response.
curl -o /dev/null -sw "%{http_code}" $1
