from collections import namedtuple
#output file paths
DataIngestionArtifact = namedtuple("DataIngestionArtifact",["train_file_path","test_file_path","is_ingested", 
                                    "message"])