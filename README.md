# Airflow DAG Creator

A Flask-based web application that provides an interface to create and manage Apache Airflow DAGs through a REST API and web interface.

## Features

- Create DAG runs with custom configurations
- Web interface for DAG management
- RESTful API endpoints
- Dynamic configuration key-value pairs

## Prerequisites

- Python 3.8+
- Flask
- Apache Airflow

## Installation

1. Clone the repository:

```bash
    git clone git@github.com:olartbaraq/Davu-Assessment.git
    cd airflow-dag-creator
```

2. Create and activate virtual environment:

```bash
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:

```bash
  pip install -r requirements.txt
```

4. Start the Flask server:

```bash
  cd DAG/
  flask --app core run --debug --with-thread
```

5. Access the DAG Interface creation form

```bash
  http://localhost:5000/api/experimental/dags/
```
