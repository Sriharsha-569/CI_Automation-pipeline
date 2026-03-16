
# CI Automation Pipeline

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red)
![Docker](https://img.shields.io/badge/Docker-containerised-blue)
![Tests](https://img.shields.io/badge/Tests-10%20passing-green)

A real Jenkins CI pipeline connected to a Python calculator
application with automated testing and Docker containerisation.

## What Makes This Real

| Before | After |
|--------|-------|
| echo statements only | Real Python application |
| Always passes | Fails if code breaks |
| No tests | 10 pytest unit tests |
| No app | Working calculator |

## Tech Stack

| Tool      | Purpose                   |
|-----------|---------------------------|
| Jenkins   | CI/CD pipeline automation |
| Python 3  | Application language      |
| Pytest    | Unit testing framework    |
| Docker    | Containerisation          |
| Git       | Version control           |

## Project Structure
```
CI_Automation-pipeline/
├── Jenkinsfile              # Real 6 stage CI pipeline
├── requirements.txt         # Python dependencies
├── conftest.py              # Pytest configuration
├── src/
│   ├── __init__.py
│   └── calculator.py        # Python application
├── tests/
│   └── test_calculator.py   # 10 unit tests
└── docker/
    └── Dockerfile           # Container definition
```

## Run Locally
```bash
# Clone the repo
git clone https://github.com/Sriharsha-569/CI_Automation-pipeline.git
cd CI_Automation-pipeline

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ --verbose

# Run with coverage
pytest tests/ --cov=src --cov-report=term-missing
```

## Run in Docker
```bash
# Build image
docker build -t ci-automation -f docker/Dockerfile .

# Run tests inside container
docker run ci-automation
```

## Jenkins Pipeline Stages
```
Stage 1 → Checkout   Clone repo from GitHub
Stage 2 → Setup      Install Python dependencies
Stage 3 → Lint       Check code syntax
Stage 4 → Test       Run 10 pytest unit tests
Stage 5 → Build      Build Docker image
Stage 6 → Deploy     Run container
```

## Test Results
```
tests/test_calculator.py::test_add_positive_numbers   PASSED
tests/test_calculator.py::test_add_negative_numbers   PASSED
tests/test_calculator.py::test_subtract               PASSED
tests/test_calculator.py::test_multiply               PASSED
tests/test_calculator.py::test_divide                 PASSED
tests/test_calculator.py::test_divide_by_zero         PASSED
tests/test_calculator.py::test_percentage             PASSED
tests/test_calculator.py::test_percentage_zero_total  PASSED
tests/test_calculator.py::test_add_floats             PASSED
tests/test_calculator.py::test_multiply_by_zero       PASSED

10 passed in 0.12s
```

## Author

**Sri Harsha Deep Chilakalapudi**
Hof University of Applied Sciences — MSc Software Engineering
[GitHub](https://github.com/Sriharsha-569) 
