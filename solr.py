import os
import pysolr


class Solr:
    def __init__(self):
        self.client = pysolr.Solr(os.getenv("SOLR_BASE_URL"))
        self.client.ping()
