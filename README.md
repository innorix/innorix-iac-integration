# INNORIX IaC Integration

Official integration examples for bootstrapping infrastructure with INNORIX after Infrastructure as Code provisioning.

## Supported Platforms

- Terraform
- Pulumi
- Crossplane
- Upbound
- Spacelift
- env0

## Features

- Bootstrap newly provisioned infrastructure
- Distribute large datasets and application assets
- Automate initial file deployment
- Track transfer progress using the INNORIX REST API
- Verify transfer completion

## Repository Structure

```text
.
├── client.py
└── integrations/
    ├── terraform/
    ├── pulumi/
    ├── crossplane/
    ├── upbound/
    ├── spacelift/
    └── env0/
```

## Workflow

```text
Infrastructure Provisioning
        │
Terraform / Pulumi / Crossplane
        │
Infrastructure Ready
        │
        ▼
INNORIX Bootstrap
        │
Large Dataset
Application Package
Initial Data
        │
        ▼
Deployment Complete
```

## Requirements

- Python 3.10+
- INNORIX Platform
- INNORIX API Key

## Installation

```bash
pip install -r requirements.txt
```

Copy the example configuration.

```bash
cp .env.example .env
```

Update the configuration.

```text
INNORIX_BASE_URL=
INNORIX_API_KEY=
SOURCE_DEVICE_ID=
TARGET_DEVICE_ID=
TARGET_PATH=
BOOTSTRAP_PATH=
BOOTSTRAP_SIZE=
AUTOMATION_ID=
```

Run the bootstrap example.

```bash
cd integrations/terraform

python bootstrap.py
```

The same example is applicable to all supported IaC platforms.

## License

Commercial License

Copyright © INNORIX Co., Ltd. All rights reserved.