# Helmet Detection using PyTorch

 This data science project utilizes the power of PyTorch to develop a helmet detection system. The dataset for developing and testing the application is used from [kaggle](https://www.kaggle.com/datasets/andrewmvd/helmet-detection). The data is uploaded on Amazon S3 and then downloaded, augmentated and the model is trained and the trained model is then deployed to S3.

This project contains an end to end ML project lifecycle as described below. 
1. Data collection, annotation([labelImg](https://github.com/HumanSignal/labelImg)) and transformation/augmentation. (Used [Albumnetation](https://albumentations.ai) for image augmentations)
2. Model building(In this case pre-training).
3. Model training: Used Pretrained Faster-R-CNN MobilenetV3 Model. Changed the output layers as per need of only 2 classes as this model was trained for 90 classes.
4. The trained best model is then uploaded to S3 bucket and it will be used while prediction of outputs.
5. A simple REST endpoint is created using FastAPI to train and predict.


