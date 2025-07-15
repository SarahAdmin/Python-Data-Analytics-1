import pandas as pd
df = pd.read_csv('HMCTS_MI_output_accessible10.csv',encoding='latin-1')
df.style.background_gradient(cmap='Reds')
