# Contributing

## Development

Run CI locally:
```bash
# Install act: https://github.com/nektos/act
act -j test --container-architecture linux/amd64
```

Run lint locally:
```bash
act -j lint --container-architecture linux/amd64
```

## Guidelines

- Follow PEP 8 style guide
- Write tests for new features
- Ensure CI passes before submitting PR