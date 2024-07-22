import pandas as pd
from solr import Solr


class SearchService:
    def __init__(self):
        self._solr = None

    @property
    def solr(self) -> Solr:
        if self._solr is None:
            self._solr = Solr()
        return self._solr

    def search(self):
        pass

    def upload_data(self, df: pd.DataFrame):
        pass
