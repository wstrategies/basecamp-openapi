#!/bin/bash


# This script generates the SDK for the Basecamp4 API using the OpenAPI Generator
root_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; cd .. ; pwd -P )
schema_path=$root_path/schema/schema.yaml
sdk_path=$root_path/sdk/python

# Remove existing SDK
rm -rf $sdk_path

# Generate SDK using openapi-generator https://github.com/OpenAPITools/openapi-generator
openapi-generator generate -i $schema_path -g python -o $sdk_path --additional-properties=packageName=basecamp4_python_sdk