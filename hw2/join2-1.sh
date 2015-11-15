hadoop jar /opt/cloudera/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0-cdh5.4.4.jar -input input2 -output output_join2_1 -mapper join2_mapper.py -reducer join2_reducer.py -numReduceTasks 1
