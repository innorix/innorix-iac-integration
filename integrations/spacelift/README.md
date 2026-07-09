# Spacelift

This example demonstrates how to bootstrap newly provisioned infrastructure using INNORIX.

## Overview

After infrastructure provisioning is completed, INNORIX transfers large datasets, application packages, or initial bootstrap data to the target environment.

## Workflow

```text
Spacelift Run
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

## Run

```bash
python bootstrap.py
```