import pandas as pd

df_GBl = pd.read_excel("Predictions_CE_EB_GBERTLarge.xlsx")
df_GBl_masked = pd.read_excel("model_evaluation_Occlusion_CE_EB_GBERTlarge.xlsx")

#adding the model name to identify particular  model's prediction
df_GBl['model'] = 'GBERT_large'
df_GBl_masked['model'] = 'GBERT_large_masked'

# renaming the predicted label
df_GBl.rename(columns={'predicted': 'response'}, inplace=True)
df_GBl_masked.rename(columns={'Predicted Label': 'response'}, inplace=True)


#checking if the model prediction and ground truth matches
df_GBl['correct'] = (df_GBl['actual'] == df_GBl['response']).astype(int)
df_GBl_masked['correct'] = (df_GBl_masked['Actual Label'] == df_GBl_masked['response']).astype(int)

# selecting only columns required for GLMER model
df_GBl = df_GBl[['student_id', 'question_id', 'model', 'response', 'correct']]
df_GBl_masked = df_GBl_masked[['student_id', 'question_id', 'model', 'response', 'correct']]

# Combining the dataframes to get a single prediction file for GLMER model
df_combined = pd.concat([df_GBl, df_GBl_masked])

# output the required csv file
df_combined.to_csv('Occlusion_CE.csv', index=False)