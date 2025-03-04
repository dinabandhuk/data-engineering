# data-engineering

data engineering project

## requirements

- Make sure the `$AIRFLOW_HOME` variable points to your project directory so that DAGS can be conveniently placed in `project-directory/dags` rather than `~/airflow/` which is the default setting.In my case this line was added to `~/.bashrc`

```bash
export AIRFLOW_HOME=/home/mounam/projects_etc/data-engineering/airflow/
```

- This makes it convenient to edit the configuration files and add custom dags in a centralized project repository.

- Make sure **python 3.12.1** is the version in the virtual environment. Other python versions break.\
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

- just run `airflow` once in the terminal so it initializes files and folders
- change the `data-engineering/airflow/airflow.cfg`  config to point to

```bash
dags_folder = /home/mounam/projects_etc/data-engineering/dags
```

instead of

```bash
dags_folder = /home/mounam/projects_etc/data-engineering/airflow//dags
```

because `data-engineering/airflow` is in gitignore but we want the dag files to be tracked by git.
`data-engineering/dags` is tracked so we keep our DAGs there.

- create a root user with given parameters

```bash
airflow users create --username root --password root1234 --firstname root --lastname root --role Admin --email root@gmail.com
```

- start the webserver and scheduler

```bash
airflow webserver
airflow scheduler
```

- resolve dag not being recognized after deleting from the web interface

```bash
airflow db shell
```

```bash
UPDATE dag SET is_active=True, is_paused=False WHERE dag_id='your_dag_id';
```
