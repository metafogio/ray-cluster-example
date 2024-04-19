from collections import Counter
import socket
import time

import ray

#Change the IP with your Metafog Cluster Head Node IP
ray.init(_node_ip_address='100.64.XXX.XXX')

print('''This cluster consists of
    {} nodes in total
    {} CPU resources in total
'''.format(len(ray.nodes()), ray.cluster_resources()['CPU']))

@ray.remote
def f():
    time.sleep(0.001)
    return socket.gethostbyname(socket.gethostname())

object_ids = [f.remote() for _ in range(1000)]
ip_addresses = ray.get(object_ids)

print('Tasks executed')
for ip_address, num_tasks in Counter(ip_addresses).items():
    print('    {} tasks on {}'.format(num_tasks, ip_address))
