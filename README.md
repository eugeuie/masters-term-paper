# Развитие методов классификации и оценки значимости признаков на основе случайных лесов в контексте задачи картографирования земного покрова России

## Overview

Институт: [Институт космических исследований Российской академии наук](https://iki.cosmos.ru/)

Отдел: [Технологии спутникового мониторинга](http://smiswww.iki.rssi.ru/)

Научный руководитель: [к.т.н. Хвостиков Сергей Антонович](http://smiswww.iki.rssi.ru/default.aspx?page=39&empid=40)

Данные: https://1drv.ms/u/s!AvoMv5a1kmNwpxVI1T0yDoBTmLvJ?e=vWkab0

### Articles

[Краткая статья по картографированию растительности России и методам лаборатории](https://github.com/eugeuie/masters-term-paper/blob/main/articles/(annotated)%20%D0%91%D0%B0%D1%80%D1%82%D0%B0%D0%BB%D0%B5%D0%B2%20-%20%D0%A1%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B5%20%D0%B8%20%D0%BF%D0%B5%D1%80%D1%81%D0%BF%D0%B5%D0%BA%D1%82%D0%B8%D0%B2%D1%8B%20%D1%80%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D1%8F%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D0%BE%D0%B2%20%D1%81%D0%BF%D1%83%D1%82%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE%20%D0%BA%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20%D1%80%D0%B0%D1%81%D1%82%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BF%D0%BE%D0%BA%D1%80%D0%BE%D0%B2%D0%B0%20%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8.pdf)

[Детальный обзор методов лаборатории, вопросы картографирования начинают обсуждаться со страницы 93 (стр. 95-96 можно пропустить)](https://github.com/eugeuie/masters-term-paper/blob/main/articles/(annotated)%20%D0%91%D0%B0%D1%80%D1%82%D0%B0%D0%BB%D0%B5%D0%B2%20-%20%D0%A1%D0%BF%D1%83%D1%82%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%BA%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%80%D0%B0%D1%81%D1%82%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BF%D0%BE%D0%BA%D1%80%D0%BE%D0%B2%D0%B0%20%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8.pdf)

[Обзорная статья по применению случайных лесов к ДЗЗ](https://github.com/eugeuie/masters-term-paper/blob/main/articles/(annotated)%20Belgiu%2C%20Dr%C4%83gu%C5%A3%20-%20Random%20forest%20in%20remote%20sensing.pdf)

## Tech Details

### Large Datasets

При попытке загрузить набор данных `lc_sample.csv` с помощью Pandas получаем ошибку `MemoryError: Unable to allocate 7.72 GiB for an array with shape (14, 74029669) and data type int64`.

[Pandas: Scaling to large datasets](https://pandas.pydata.org/pandas-docs/stable/user_guide/scale.html)

[Kaggle: Tutorial on reading large datasets](https://www.kaggle.com/rohanrao/tutorial-on-reading-large-datasets)

[GitHub: Vaex: a Python library for lazy Out-of-Core DataFrames (similar to Pandas), to visualize and explore big tabular datasets](https://github.com/vaexio/vaex)

[Towards Data Science: ML impossible: Train 1 billion samples in 5 minutes on your laptop using Vaex and Scikit-Learn](https://towardsdatascience.com/ml-impossible-train-a-1-billion-sample-model-in-20-minutes-with-vaex-and-scikit-learn-on-your-9e2968e6f385)

[Towards Data Science: How to analyse 100 GB of data on your laptop with Python](https://towardsdatascience.com/how-to-analyse-100s-of-gbs-of-data-on-your-laptop-with-python-f83363dda94)

### Model Persistence

[sklearn: Model persistence](https://scikit-learn.org/stable/modules/model_persistence.html)

[sklearn-onnx: Convert your scikit-learn model into ONNX](https://onnx.ai/sklearn-onnx/)

[sklearn: OOB Errors for Random Forests](https://scikit-learn.org/stable/auto_examples/ensemble/plot_ensemble_oob.html)

### Confusion Matrix

[Wikipedia: Confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix)