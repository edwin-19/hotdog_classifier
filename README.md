# Hotdog classifier end to end
This repo is a test to build an END TO END pipeline deep learning for tensorflow 2

- The point is to test out a few concepts for tensorflow 2 keras
    - Keras tuner
    - TF Dataset

## Dataset
Dataset used was from kaggle, which is just a subset of food 101 dataset

You download [here](https://www.kaggle.com/dansbecker/hot-dog-not-hot-dog)

## TODO
- [x] Compare sequence to tf dataset api
- [x] Write using the subclass api for model
- [x] Write custom loop with gradient tape api
- [ ] Use keras tuner for hyperparam tuning
- [ ] Use hiplot to visualize training
- [ ] Convert model to tflite and port to android
- [x] Write web code for deployment
- [x] Write benchmark code for deployment