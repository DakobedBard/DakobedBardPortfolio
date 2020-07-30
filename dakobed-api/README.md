### Dakobed Serverless API

Test query params.. 
location=Trinity&sdate=20140101&edate=20140102

curl --request POST -H "Content-Type: application/audio"  --data-binary "@/home/mddarr/data/DakobedBard/dakobed-serverless-api/style.jpg" \
    https://nn04nyh2j5.execute-api.us-west-2.amazonaws.com/v1/upload
    


# Layers

### Zip the layer
zip -r ./model-layer.zip ./python

zip -r ./librosa-layer.zip ./l

https://github.com/antonpaquin/Tensorflow-Lambda-Layer