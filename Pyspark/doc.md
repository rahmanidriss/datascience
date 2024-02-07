# Pyspark
[how many executor you'll be assign for 10 GB i HDFS ?](#number-of-executors) 

[Amount of memory required for each executor ?](#executor) 

1. [Conditional Functions](#Conditional)
2. [Normal and Misc functions](#misc)

### <a id="number-of-executors"></a>how many executor you'll be assign for 10 GB i HDFS ? 

|1. Find the number of partitions:| 10 X 1024 MB/128 MB = 80 partitions|
|-----|--------|
|2. Find the CPU for maximum parallelism:| 80 cores ( 1 core -->1 partition) |
|3. Find maximun allowed CPU cores for each executor:| 5 cores per executor for YARN|
|4. Number of executors = Total Cores/executor cores:| Total cores(80)/ executor cores(5) = 16|

[essential](https://medium.com/@uzzaman.ahmed/pyspark-window-functions-a-comprehensive-guide-dc9bdad8c7ae)

### <a id="executor"></a> Amount of memory required for each executor ?

|1. Partition size :| Default partion size split 128MB|
|-----|--------|
|2. Assign a minimum 4xmemory for each core| 128 x 4 = 512MB|
|3. Multiply it by by executor cores to get executor memory| 512 x 5 =256O MB ( round it to 3 GB)|

## PySpark - Built-in Functions 
``` python
from pyspark.sql.functions import skewness, kurtosis, var_pop, var_samp, stddev, stddev_pop, sumDistinct, ntile, udf, col, desc
from pyspark.sql.functions import split, explode, substring, upper, trim, lit, length, regexp_replace, col, when, desc, concat, coalesce, countDistinct, expr
```
## Spark
 - sparkSession
   - sparkContext
     - uiWebUrl
     - setLogLevel
     - .
     - .
   - 
## Data Serialization
    - Java Serialisation (default)
    - Kryo serialization 


### <a id="Conditional"></a>Conditional Functions   
  
1. WHEN
2. FILTER
3. CASE
4. WHEN().OTHERWISE()

### <a id="misc"></a>Normal and Misc functions
1. COALESCE
2. CRC32
3. ENCODE
4. DECODE
5. GREATEST 
6. LEAST
7. IFNULL
8. NULLIF
9. NANVL
10. RAND
11. RANDN
12. SPARK_PARTITION_ID
13. INPUT_FILE_NAME
14. RAISE

### Hash Functions
1. HASH
2. MD5
3. SHA1
4. SHA2

### Aggregate Window 
1. COLLECT_LIST
2. COLLECT_SET
3. CORR
4. COVAR_POP
5. COVAR_SAMP
6. FIRST_VALUE
7. LAST_VALUE
8. PERCENTILE_CONT
9. PERCENTILE_DISC
10. STDDEV_POP
11. STDDEV_SAMP
12. SUM
13. VARIANCE

### Mathematical Functions
1. ABS
2. CEIL
3. FLOOR
4. ROUND
5. EXP
6. LOG
7. SQRT
8. POW
9. MAX & MIN
10. HEX & BIN

### Window Functions
1. ROW_NUMBER
2. RANK
3. DENSE_RANK
4. PERCENT_RANK
5. LEAD
6. LAG
7. FIRST
8. LAST
9. NTH
10. CUME_DIST

### Collection Functions https://spark.apache.org/docs/latest/api/sql/
1. ARRAY_CONTAINS
2. ARRAY_SORT
3. ARRAY_UNION
4. ARRAY_INTERSECT
5. FILTER
6. SLICE
7. EXPLODE
8. SIZE
9. FROM_JSON
10. TO_JSON
11. FROM_CSV
12. TO_CSV
13. ARRAY
14. CREAT_MAP

### Date & Time Functions
1. CURRENT_DATE
2. CURRENT_TIMESTAMP
3. DATE_ADD
4. DATE_SUB
5. DATEDIFF
6. YEAR
8. MONTH
9. DAYOFMONTH
10. HOUR
11. MINUTE
12. SECOND
13. FROM_UNIXTIME
14. UNIX_TIMESTAMP
15. TO_TIMESTAMP
16. TO_DATE
17. TRUNC
18. MONTHS_BETWEEN

### String Functions
1. CONCAT
2. CONTAINS
3. STARTSWITH
4. ENDSWITH
5. INITCAP
6. UPPER
7. LOWER
8. SUBSTRING
9. LENGTH
10. LPAD
11. TRIM
12. LTRIM
13. RTRIM
14. REGEX_EXTRACT
15. REGEX_REPLACE
16. RPAD
17. SPLIT

### Aggregate Functions
1. SUM
2. COUNT
3. AVG
4. MAX
5. MIN
6. GROUP BY

## [Pandas UDFs in PySpark ](https://medium.com/@suffyan.asad1/an-introduction-to-pandas-udfs-in-pyspark-a0a512bd00e2)

[Spark Memory Management ](https://community.cloudera.com/t5/Community-Articles/Spark-Memory-Management/ta-p/317794)

## join in pyspark
        joinCondition=df1.col("id1")===df2.col("id2")
    - inner join : df1.join(df2, joinCondition) 
    - 



## Prtition
 - repartition control the number of partitions( memory only)
 - coalesce reduce the number of partitions without shuffling data (memory only)
 - partitionBy (save in disk)
## [Best practice](https://umbertogriffo.gitbook.io/apache-spark-best-practices-and-tuning/)

## [join](<https://medium.com/plumbersofdatascience/exploring-the-different-join-types-in-spark-sql-a-step-by-step-guide-49342ffe9578>)


# garbage collection 

>  prevent memory leaks 
- 1 GC (default)
- 2 G1 GC (recommanded for machines with may cores )

# Data Skew
cause : 

    - Join operations (except Boradcast-Hash join)
    - Grouping and aggregating 




    https://youtu.be/zXsOcrsLk7g

documented, readable code  
safer run-time behaviour  
simplifier  debugging and testing 

## large number of small files
- Reduce parallelism
- Reduce shuffle partitions before writing a dataframe

## [Apache Spark – Performance Tuning and Best Practices](https://dataforgeeks.com/apache-spark-performance-tuning-and-best-practices/2305/)

 spillListener = spark._jvm.org.apache.spark.SpillListener()
    print(spillListener.numSpilledStages())

UDF
https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/5437916721496700/1514640156683959/8171343853200382/latest.html

## spark data scientist https://haya-toumy.gitbook.io/spark-notes/pyspark/pyspark/catch-it-all-page


[basic spark configuration](https://towardsdatascience.com/basics-of-apache-spark-configuration-settings-ca4faff40d45)

- Cluster Parameters
 - size 
 - instance type
   - of processors
   - of memory
 - Disk
 ...

- Spark configuration:
 - parallelism (spark.sql.shuffle.partitions or adaptive execution)
 - Shuffle
   - shuffle spill
     issues: the deserialised data produced by the map stages in a shuffle does not fit in memory 
     fix: 
     1. reduce the input data of each task by reducing the umber of partitions
     2. ecrease the meory avaible to each task
       - by incerasing spark executor memory
       - decreasig the number of cores per executor
 - Storage
 - JVM tuning
 - Feature flags
 - ...

 - of partition: 3x number of cores in the cluster
 - of cores per executor: 4-8
 - memory per executor 85% *(node memory/executor by node)

### Adaptive Query Execution (AQE) Optimizer

https://kyuubi.readthedocs.io/en/v1.6.1-incubating/deployment/spark/aqe.html

# Enable AQE
spark.conf.set("spark.sql.adaptive.enabled", "true")