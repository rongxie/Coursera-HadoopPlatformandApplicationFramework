show_views_file = sc.textFile("input2/join2_gennum?.txt")


def split_show_views(line):
    s = line.split(",")
    show = s[0]
    views = int(s[1])
    return (show, views)

show_views = show_views_file.map(split_show_views)

show_channel_file = sc.textFile("input2/join2_genchan?.txt")

def split_show_channel(line):
    s = line.split(",")
    show = s[0]
    channel= s[1]
    return (show, channel)

show_channel = show_channel_file.map(split_show_channel)

joined_dataset = show_channel.join(show_views)

def extract_channel_views(show_views_channel):
    print(show_views_channel) 
    channel = show_views_channel[1][0]
    views = show_views_channel[1][1]
    return (channel, views)

Now you can apply this function to the joined dataset to create an RDD of channel and views:

channel_views = joined_dataset.map(extract_channel_views)

def some_function(a, b):
    some_result = a + b
    return some_result

channel_views.reduceByKey(some_function).collect()

