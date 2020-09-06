# Secure Semantic Search over Encrypted Big data in the Cloud (S3BD)

## Introduction
This is an open-source program that enables semantic enterprise search for unstructured encrypted big datasets stored in the cloud. 
If you are using this tool in your research projects, please cite the following paper:
```
@article{woodworth2019s3bd,
  title={S3BD: Secure semantic search over encrypted big data in the cloud},
  author={Woodworth, Jason W and Amini Salehi, Mohsen},
  journal={Concurrency and Computation: Practice and Experience},
  volume={31},
  number={11},
  pages={e5050},
  year={2019},
  publisher={Wiley Online Library}
}
```
The paper is also available in the following address:
http://hpcclab.org/paperPdf/ccpe18/ccpe18.pdf

## Set up
1. Clone S3BD. ```git clone https://github.com/hpcclab/S3BD.git```  
2. Go to S3Bd folder and provide read, write, and execute permission to all. ```chmod a+x *```
3. Command ```./execute.sh``` to build required folders and load the upload folder with dataset.
 
## S3BD Running Instructions

S3BD is composed of two projects named ```ClientEncryptedSearch``` and ```EncryptedSearchServer``` that act as client and cloud respectively.  
These two can be run on the same machine, or on two machines connected by a network.  There are three primary actions you can perform when running the system: Uploading documents, Partitioning the dataset into clusters, and Searching over the dataset.

## Uploading Documents

1. To start an upload, launch the cloud server and select upload as its action (the ``` -u ``` flag) in IDE (e.g., Eclipse) console.
2. Choose how they'll be uploaded based on your project configuration. Default:
   input ```-n```, hit enter  to upload files through network.
3. Once the server is running, launch the client and select upload as its action (again, the ``` -u ``` flag).  
4. To perform a batch upload, enter the path for the directory with the files. Command: ```data/tmp``` to upload demo dataset. Single file uploads are not currently supported.

5. After finishing the uploads, go to S3BD->cloudserver->utilities location. Check index.txt and docsizes.txt files. They should be filled with recent update.


## Partitioning Dataset

1. To start partitioning the dataset, launch the cloud server and select partition as its action (the ``` -p ``` flag).  
2. The process will start automatically.  The console will display the progress of the partitioning. Once the IDE console notes that ```it is ready to connect to the client```, launch the client, select partitioning by providing ```-p``` as its action, and the files will be transferred.

## Searching

1. To start a search, launch the cloud server and select search as its action (the ``` -s ``` flag).  The cloud will begin loading relevant data.

2. Once the server is ready to accept a search, launch the client and select search as its action by ```-s``` flag, then enter the desired search query.  The client's console should soon show the results of the search. Example queries: ```host network, network protocol, internet engineering, routing protocol```

## Configuration details.

The config files for each project can be found in the utilities subdirectory of the src directory.  Most importantly:

### Client Project

  * cloudIP - the IP used to connect to the server. Use localhost if both projects are local.
  * socketPort - the socket used for data transfers. Ensure this is the same on both client and cloud.
  * calcMetrics - only set this to true if you are testing speeds.
  * numSearchedAbstracts - determines the number of abstracts and clusters that should be searched over.  Has a heavy impact on speed and accuracy.
  
### Cloud Project

  * socketPort - the socket used for data transfers.  Ensure this is the same on both client and cloud.
  * abstractIndexCound - the number of terms that will be included in an abstract index.
  * k - the number of clusters created during partitioning.
  * calcMetrics - only set this to true if you are testing speeds.

## How to Contribute
We welcome new features, extension, or enhancements of S3BD.

We are, in particular, looking for new collaborations, taking this framework further. As extension of S3C, we have developed S3BD that is similar to S3C but can perform search over encrypted Big Data. In addition to S3BD, we are also researching to extend the capabilities of S3BD such as search query expansion, intelligent pruning, clustering, and so on. Please drop us an email if you are interested to collaborate. 

## Contacts
* [Dr. Mohsen Amini Salehi](http://hpcclab.org/index.php/contact-us/)
* [Jason Woodworth](https://vrlab.cmix.louisiana.edu/people/jason-woodworth/)
* [SM Zobaed](zobaedsakib@gmail.com)
  
 ## Acknowledgements
 This project is derived from Jason Woodworth Master's thesis. In addition to the code base, the project includes his thesis latex files too.

