rm -r -f cloud
rm -r -f S3BD_client_unmodified/data/abstracts
rm -r -f S3BD_client_unmodified/data/tmp

mkdir cloud
mkdir cloud/cloudserver
mkdir cloud/cloudserver/storage
mkdir cloud/cloudserver/utilities
mkdir cloud/cloudserver/watch
mkdir cloud/cloudserver/utilities/clusters
mkdir S3BD_client_unmodified/data/abstracts
mkdir S3BD_client_unmodified/data/tmp

cp S3BD_client_unmodified/input/* S3BD_client_unmodified/data/tmp

