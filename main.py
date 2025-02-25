from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator
from datetime import datetime


def test():
    try:
        pg_hook = PostgresHook(postgres_conn_id="postgres_id")
        print("Подключение к PostgreSQL успешно")
        
        sql_query = 'SELECT * FROM "base_name";'
        result = pg_hook.get_records(sql=sql_query)
        
        print("Результаты запроса:")
        for row in result:
            print(row)
            
    except Exception as e:
        print(f"Ошибка при выполнении SQL-запроса: {e}")

with DAG(
    dag_id="test_hook",
    start_date=datetime(2023, 10, 1),
    schedule_interval="@daily",  
    catchup=False,
) as dag:

    execute_sql_task = PythonOperator(
        task_id="execute_sql",
        python_callable=test,
    )