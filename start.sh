#!/bin/bash

set -e

export FLASK_APP=kex:create_app

gunicorn -w 4 -b 0.0.0.0:${PORT:-8080} kex:create_app

sleep 5

FLASK_APP_URL="http://0.0.0.0:${PORT:-8080}"
until curl -s $FLASK_APP_URL > /dev/null; do
    echo "ᴡᴀɪᴛɪɴɢ ꜰᴏʀ ꜰʟᴀꜱᴋ ᴀᴘᴘ ᴛᴏ ꜱᴛᴀʀᴛ..."
    sleep 2
done

python3 -m VIPMUSIC
