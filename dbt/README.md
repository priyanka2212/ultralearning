## dbt Fundamentals

### What is dbt?
- dbt is 'T' in ELT i.e. **Transformation**
- Data transformation tool in datawarehouse
- Designed for modern data stack architecture

### What dbt is NOT?
- Not data ingestion/loading tool
- Not BI tool
- Doesnt have storage
- Doesnt provide compuing processing  unit. unlike Spark which provides processing unit

### dbt Products
1. **dbt Core**
    - Execute via CLI
    - Handles documentation, testing, sql files, macros etc
    
2. **dbt Cloud**
    - Built on top of dbt Core
    - Web based product
    - more features : schedule jobs, web IDE
    - free for basic usage

### Where **dbt** fits in data life cycle?
![data-life-cycle](https://github.com/priyanka2212/ultralearning/blob/main/dbt/images/data-life-cycle-2.JPG)

  - Transform data between **Landing schema** and **Structure schema**
  - Transform data between **Structure schema** and **Consumption schema**
  - Uses computation poewr of underlying data warehouse, dbt doesnt have its own computation power

### dbt Core concepts

| Directory Structure           |
|-------------------------------|
| analysis                      |
| macros                        |
| models/examples               |
| &nbsp;&nbsp;&nbsp;&nbsp;my_first_dbt_model.sql  |
| &nbsp;&nbsp;&nbsp;&nbsp;my_first_dbt_model.sql  |
| &nbsp;&nbsp;&nbsp;&nbsp;schema.yml              |
| seeds                         |
| snapshots                     |
| tests                         |
| &nbsp;&nbsp;&nbsp;&nbsp;.gitignore               |
| &nbsp;&nbsp;&nbsp;&nbsp;README.md                |
| &nbsp;&nbsp;&nbsp;&nbsp;dbt_project.yml          |


1. **MODELS**
- It is sql file with select statement
- These models are defined in .sql files
- They can reference other models or tables in datawarehouse e.g.
```sql
SELECT 
  SUM(amount) AS total_amount
FROM {{ ref('stg_payments') }}
WHERE total_amount < 0;
```

2. **MACROS**
- Code reusability like function in python
- Reusing SQL code fragments across various models
```sql
--macros/current_timestamp.sql
{% macro current_timestamp() %}
  CURRENT_TIMESTAMP
{% endmacro %}
```

```sql
-- models/my_model.sql
WITH source_data AS(
    SELECT
      id,
      name,
      {{ current_timestamp()}} AS load_time
    FROM
      {{ref('source_table')}}
)
SELECT
  *
FROM
  source_data
```

3. **TESTS**
- Generic test 
  - Predefined tests out-of-box
  - Can apply across multiple data models
  - 4 generic tests provided by dbt:
    - not_null = should never be null
    - unique = should be unique across whole table 
    - accepted_values = should only have value in predetermined list
    - relationships = shoudld have corresponding associated entry in another table
    ```yaml
    version: 2
    models:
      - name: stg_sheets_my_forecast_goals
        columns:
          - name: sales_channel
            desciption: Sales channel for forecast
            tests:
              - not_null
              - accepted_values:
                values:
                  - offline
                  - ecommerce        
    ```


- Singular test
  - custom tests
  - write own SQL to test
  - Below Singular test will ensure all oders have positive or 0 total payment amount on the stg_payments table.

  ```sql
  SELECT
    SUM(amount) AS total_amount
    FROM {{ ref('stg_payments')}}
    WHERE total_amount<0 ;
    ```

  4. **SNAPSHOTS**
    - To track slow changing dimensions over time  
    - SCD2 only