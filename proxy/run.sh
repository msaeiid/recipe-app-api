#!/bin/sh

set -e

# substitute parameters in default.conf.tpl with environment variable with the name
envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
# start nginx in foreground
nginx -g 'daemon off;'
