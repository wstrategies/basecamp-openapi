# Basecamp OpenAPI Schema and SDK

This project contains the OpenAPI schema for the Basecamp API and a generated SDK for Python.

## OpenAPI Schema

The OpenAPI schema is located in the `schema` directory. The schema is written in YAML and is based on the [Basecamp API documentation](https://github.com/basecamp/bc3-api/tree/master)

## SDK

The SDK is generated using the [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator)

## Development

To generate the SDK, run the following command:

```bash
./bin/generate_python_sdk.sh
```
