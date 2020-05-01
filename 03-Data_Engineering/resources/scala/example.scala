import com.hortonworks.hwc.HiveWarehouseSession
import org.apache.spark.sql.SparkSession


// Create hive warehouse connector to connect to hive managed table
val hive = HiveWarehouseSession.session(spark).build()

// Build the sparkSession and set application name from config file
val spark = SparkSession
  .builder()
  .appName("Example")
  .getOrCreate()

// Setting LogLevel for the sparkContext from config file
spark.sparkContext.setLogLevel("INFO")

// Create variables with the table names
val table1_name = "default.sample_07"
val table2_name = "default.sample_08"

// Pull the data into dataframes
val query1 = "select * from %s" format (table1_name)
val query2 = "select * from %s" format (table2_name)
val t1_buff = hive.sql(query1)
val t2_buff = hive.sql(query2)

// Create alias for the tables so they can be used in joins 
val t1 = t1_buff.alias("t1")
val t2 = t2_buff.alias("t2")

// Do a simple filter on a table     
val filtered = t1.filter("salary > 50000")
filtered.show()

//Do a join of two tables
val joined = t1.join(t2, $"t1.code" === $"t2.code")
joined.show()
    
//Pipeline multiple functions, a join and a filter
val combined = t1.filter("salary > 50000").join(t2, $"t1.code" === $"t2.code")
combined.show()



