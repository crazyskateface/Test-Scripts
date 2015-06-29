"""
    This nifty little python script downloads metric data(json) from a s3 bucket and then uploads the data 
    to my public s3 bucket in a nice neat report format.
    
    report file: 
        http://test-boettjer.s3-website-us-east-1.amazonaws.com/report.txt
        
    this script file:
        http://test-boettjer.s3-website-us-east-1.amazonaws.com/s3_exersize.py
"""


from boto.s3.connection import S3Connection
import boto
from boto.s3.key import Key
import os
import requests
import json

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_KEY_ID']

# string for the report 
report_str = "Metric Data Report:\n\n"


def upload_report_to_s3():
    # create connection to s3 bucket
    conn = S3Connection(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket('test-boettjer')
    # create key for bucket
    k = Key(bucket)
    # set name of key (file)
    k.key = 'report.txt'
    # set the contents of the file being uploaded
    global report_str
    k.set_contents_from_string(report_str)
    # set metadata to the text file
    k.set_metadata('Content-Type', 'text')
    # make the file public
    k.set_acl('public-read')
    # download report with http://test-boettjer.s3-website-us-east-1.amazonaws.com/report.txt

def printable(host_dict, name):
    ret_str = name+"\n"
    ret_str += "-"*40
    ret_str += "\n"
    for host in host_dict:
        ret_str += "\n\tHost: "+str(host["host"])
        for k,v in host.iteritems():
            if not k == 'host':
                ret_str += "\n\t\t"+str(k)+": "+str(v)
    return ret_str
    
def download_info():
    # set the url to download from
    page = "https://s3.amazonaws.com/putcompanynamehere/metrics.json"
    r = requests.get(page)
    hosts = ""
    if r.status_code == 200:
        hosts = json.loads(r.content)
    
    # get objects (dicts) that have replication_lag > 200
    hosts_rep_lag = []
    hosts_ingest_rate = []
    hosts_failed_sends = []
    for host in hosts:
        if host['metric'] == 'replication_lag' and host['value'] > 200:
            hosts_rep_lag.append(host)
        elif host['metric'] == 'ingest_rate_ms' and host['value'] < 100:
            hosts_ingest_rate.append(host)
        elif host['metric'] == 'failed_sends' and host['value'] > 20:
            hosts_failed_sends.append(host)
            
    global report_str
    
    report_str += printable(hosts_rep_lag, "Hosts with Replication Lag above 200 -")
    report_str += "\n\n" + printable(hosts_ingest_rate, "Hosts with Ingestion Rate lower than 100 -")
    report_str += "\n\n" + printable(hosts_failed_sends, "Hosts with Failed Sends above 20 -")
    
    

def main():
    
    print("Downloading report")
    download_info()
    print("Uploading report to s3 bucket - test-boettjer")
    upload_report_to_s3()
    print("Finished uploading report")
    

if __name__ == "__main__":
    main()






