import numpy as np

from sotabencheval.image_classification import ImageNetEvaluator

evaluater = ImageNetEvaluator(
            model_name='MobileNet-v2',
            paper_arxiv_id='1801.04381')

with open('mobilenet_v2_imagenet.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        image_id, preds = line.split(":")
        image_id = image_id.rstrip().lstrip()
        preds = preds.lstrip().rstrip()
        preds = np.fromstring(preds, dtype=float, sep=' ')
        
        evaluater.add({image_id : preds})

    evaluater.get_results()
