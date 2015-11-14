hadoop jar /opt/cloudera/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0-cdh5.4.4.jar -input input -output output_join -mapper join1_mapper.py -reducer join1_reducer.py
