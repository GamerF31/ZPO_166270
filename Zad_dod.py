import numpy as np
import pandas as pd

def eliminate_correlated_features(data, correlation_threshold):
    corr_matrix = data.corr()
    to_drop = []
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > correlation_threshold:
                colname = corr_matrix.columns[i]
                if colname not in to_drop:
                    to_drop.append(colname)
    data_dropped = data.drop(columns=to_drop)
    return data_dropped, to_drop

data = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [1, 3, 2, 4, 5],
    'D': [2, 3, 4, 5, 6]
})

correlation_threshold = 0.9
cleaned_data, dropped_columns = eliminate_correlated_features(data, correlation_threshold)

print("Usunięte zmienne:", dropped_columns)
print("Pozostałe dane:")
print(cleaned_data)
