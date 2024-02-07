[Spark Join Strategies — How & What?](https://towardsdatascience.com/strategies-of-spark-join-c0e7b4572bcf)
[spark doc](https://spark.apache.org/docs/latest/sql-performance-tuning.html#join-strategy-hints-for-sql-queries)

[Performance improving techniques to make Spark Joins 10X faster](https://medium.com/analytics-vidhya/4-performance-improving-techniques-to-make-spark-joins-10x-faster-2ec8859138b4)

- Broadcast Join (spark.sql.autoBroadcastJoinThreshold)
- Sort Merge Join
  1. Shuffle partitions: spark.sql.shuffle.partitions (200 default)
        - Partition identifier for a row is determined as Hash(join key)% 200 
        - This type of repartitioning is called HashRepartitioning. Hash is computed by default using the .hashcode() method in java.

  2. Sorting within each partition
  3. Join the sorted partitions