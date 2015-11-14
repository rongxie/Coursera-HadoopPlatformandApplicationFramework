hadoop jar /opt/cloudera/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0-cdh5.4.4.jar -input input -output output_new -mapper wordcount_mapper.py -reducer wordcount_reducer.py
