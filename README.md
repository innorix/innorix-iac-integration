# INNORIX IaC Integration

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Infrastructure as Code](https://img.shields.io/badge/Infrastructure-IaC-6C63FF)
![Terraform](https://img.shields.io/badge/Terraform-Supported-844FBA)
![Pulumi](https://img.shields.io/badge/Pulumi-Supported-8A3391)
![License](https://img.shields.io/badge/License-Commercial-red)
![Status](https://img.shields.io/badge/Status-Official-success)

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