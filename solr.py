import os
import pysolr


class Solr:
    def __init__(self):
        self.collection_name = "apsiyon"
        self.client = pysolr.SolrCloud(
            zookeeper=pysolr.ZooKeeper(os.getenv("ZK_HOST")),
            collection=self.collection_name,
        )
        self.client.ping()

    def search(self):
        pass
