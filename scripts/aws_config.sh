#!/usr/bin/env bash

mkdir -p ~/.aws

cat > ~/.aws/credentials << EOL
[default]
aws_access_key_id = ${AWS_ID}
aws_secret_access_key = ${AWS_KEY}
EOL