from diagrams import Cluster, Diagram
from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda
from diagrams.aws.analytics import GlueCrawlers
from  diagrams.onprem.analytics import Hive
from diagrams.onprem.analytics import Presto
from diagrams.onprem.client import Users
from diagrams.generic.database import SQL


with Diagram("Exercise 3", show=False):

    endpoint = Lambda("3rd party endpoint")

    with Cluster("orchestration"):

        raw_data = S3("raw_data")

        transformed_data = S3("compressed data")

        crawler = GlueCrawlers("crawler")
    
    presto = Presto("presto db")
    
    hive = Hive("DW")

    ds_team = Users("users")

    redash_ui = SQL("redash_ui")

    endpoint >> raw_data
    raw_data >> transformed_data
    crawler >> transformed_data
    crawler >> hive
    hive >> crawler
    presto >> hive
    redash_ui >> presto
    ds_team >> redash_ui

    # TLDR
    """
    * pull data through http request
    * dump data as is in into s3
    * transform raw and dump into another folder
    * have a crawler to read that data and insert into hhive
    * use hive connector to make data available in presto
    * use redash as ui to query data from presto
    * orchestration can be done with airflow including error handling and whatnot
    """