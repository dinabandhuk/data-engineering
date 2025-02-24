# data-engineering
data engineering project

## requirements
Make sure **python 3.12.1** is the version in the virtual environment. Other python versions break.\
**Don't** install with the following constraints:
```bash
pip install 'apache-airflow[postgres,slack,celery]==2.10.4' --constraint "https://raw.git
hubusercontent.com/apache/airflow/constraints-2.10.4/constraints-3.8.txt"
```
just install as: finally a working method where everything works
```bash
pip install "apache-airflow[postgres,slack,celery]==2.10.5" 
```

```bash
pip install pandas faker pgadmin4
```

- create a root user with given parameters
```bash
airflow users create --username root --password root1234 --firstname root --lastname root --role Admin --email root@gmail.com
```
