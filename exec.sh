rm -r -f cloud
rm -r -f ClientEncryptedSearch/data/abstracts
rm -r -f ClientEncryptedSearch/data/tmp

mkdir cloud
mkdir cloud/cloudserver
mkdir cloud/cloudserver/storage
mkdir cloud/cloudserver/utilities
mkdir cloud/cloudserver/watch
mkdir cloud/cloudserver/utilities/clusters
mkdir ClientEncryptedSearch/data/abstracts
mkdir ClientEncryptedSearch/data/tmp

cp ClientEncryptedSearch/input/* ClientEncryptedSearch/data/tmp

