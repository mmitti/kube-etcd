from socket import gethostname
import netifaces
import subprocess
import os

host = gethostname()
addr = ""
for iface_name in netifaces.interfaces():
    iface_data = netifaces.ifaddresses(iface_name)
    if netifaces.AF_INET in iface_data:
        if iface_data[netifaces.AF_INET][0]['addr'] not in '127.0.0.1':
            addr = iface_data[netifaces.AF_INET][0]['addr']

cmd = "etcd --name " +host \
+" --data-dir "+os.environ["DATADIR"]\
+" --listen-client-urls http://0.0.0.0:2379 --advertise-client-urls http://"+addr+":2379" \
+" --listen-peer-urls http://0.0.0.0:2380 --initial-advertise-peer-urls http://"+addr+":2380"\
+" --discovery-fallback proxy --initial-cluster-token mytoken --discovery "+os.environ["DISCOVERY"]
print(cmd)
subprocess.call(cmd , shell=True)

#listen-client-url: "http://0.0.0.0:2379" advertise-client-urls: "http://192.168.0.11:2379"
#"listen-peer-urls: "http://192.168.0.11:2380" initial-advertise-peer-urls: "http://192.168.0.11:2380"
##ENTRYPOINT etcd -peer-addr :7001 -addr :2380 -discovery DISCOVERY=http://192.168.137.20:2379/v2/keys/discovery/test
