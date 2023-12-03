The `classification_report` function in scikit-learn provides a comprehensive summary of the performance of a classification model. It includes various metrics for each class in your target variable. The typical metrics included in the report are:

### 1. Precision:
   - Precision is the number of true positive predictions divided by the total number of positive predictions (both true positives and false positives). It measures the accuracy of the positive predictions.

### 2. Recall (Sensitivity or True Positive Rate):
   - Recall is the number of true positive predictions divided by the total number of actual positives (true positives and false negatives). It measures the ability of the model to capture all positive instances.

### 3. F1-Score:
   - The F1-score is the harmonic mean of precision and recall. It provides a balance between precision and recall. The formula is \(2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}\).

### 4. Support:
   - The support is the number of actual occurrences of the class in the specified dataset. It helps to understand the distribution of classes in the dataset.

### 5. Accuracy:
   - Accuracy is the overall correct predictions divided by the total number of predictions. It's a general measure of model performance.

### 6. Macro Average and Weighted Average:
   - For multiclass classification, the report often includes macro average and weighted average metrics, which provide an aggregate measure across all classes.

The classification report is a valuable tool for understanding how well your model is performing for each class, especially in imbalanced datasets where some classes might have fewer instances.

![Alt Text](classification_report.jpg)
