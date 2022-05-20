python3 -m sgqlc.introspection \
--exclude-deprecated \
--exclude-description \
https://test2.teletraan.io/graphql/ \
platform_schema.json || exit 1

sgqlc-codegen schema platform_schema.json platform_schema.py;
