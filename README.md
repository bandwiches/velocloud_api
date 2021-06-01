# Velocloud
A async package for interacting with Velocloud Orchestrator.

| Table of Contents |
|-------------------|
|[VCO API Version Support](#VCO-API-Version-Support)|
|[Usage](#Usage)|
|[Caveats](#Caveats)|

## VCO API Version Support
This package currently supports VCO API v4.2.1.
**This package currently supports token authentication ONLY.**

## Usage
You will need to create a VCO user with a valid API Token to use this package.
See [example.py](velocloud/example.py)

## Caveats
There is no support for building and creating Model objects from scratch (use at your own risk).  Models are strictly intended for mapping information pulled from the API.  This may or may not change over time.

## API Mapping
Modules are mapped based on their API endpoint.
- velocloud.edge = /edge
- velocloud.enterprise = /enterprise