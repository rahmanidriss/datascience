spark.shuffle.manager
Hash Partitioner uses MurMur3 hashing algorithm
spark.sql.shuffle.partition 

import mmh3
hashed_id=mmh3.hash("id")%spark.sql.shuffle.partition



## Spark Optimization [Shuffle](https://blog.devgenius.io/shuffle-in-spark-d95b5ebe7b4e)

- shuffle
 - spark.sql.shuffle.partitions (default 200) (dataframe)
 - spark.default.parallelism => RDD only
 - spark.reducer.maxMbInFlight (default 48MB)
 - spark.shuffle.compress (default Snappy) or LFZ
 - spark.shuffle.spill.compress
 - spark.shuffle.file.buffer
 - spark.io.compression.codec

 - custom  Shuffle Manager:
   - spark.shuffle.manager 1.4

 - Shuffle with Dynamic Resource Allocation:
    - spark.shuffle.service.enabled
    - spark.dynamicAllocation.shuffleTracking.enabled

[join](https://www.waitingforcode.com/apache-spark-sql/shuffle-join-spark-sql/read)

https://0x0fff.com/spark-architecture-shuffle/

?? park.sql.adaptive.coalescePartitions.minPartitionNum
https://spark.apache.org/docs/latest/sql-performance-tuning.html
https://www.cyres.fr/blog/spark-3-adaptive-query-execution-explication-et-optimisation/#Bref_historique_de_lAQE_pour_Spark

https://www.linkedin.com/pulse/apache-spark-shuffle-akhil-pathirippilly-mana/
