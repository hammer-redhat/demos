#!/bin/bash

# Check if Apache is serving web content

echo "Checking if Apache is serving web content..."

if curl -s -o /dev/null -w "%{http_code}" http://172.16.2.11/index.html | grep -q "200"; then
    echo "Apache is serving web content (HTTP 200 OK)"
else
    echo "Apache is not serving web content or is unreachable"
fi

exit 0
