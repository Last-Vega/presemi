import pandas as pd

def calc_rate(f1, f2):
    df1 = pd.read_csv(f1)
    label_list = []
    for url in df1['Input.image_url']:
        # print(url)
        label_list.append(url.split('/')[-1].split('_')[0])

    df1['label'] = label_list
    df1 = df1[['HITId', 'label']]
    df1 = df1.drop_duplicates()

    df2 = pd.read_csv(f2, delimiter='\t')
    df2 = df2.rename(columns = {'TaskID':'HITId'})

    df = pd.merge(df1, df2, on='HITId', how='inner' )
    # print(df.head())

    count = 0
    correct = 0

    for label, answer in zip(df['label'], df['Estimate_label']):
        if label == answer:
            correct += 1
        count += 1

    return correct/count


print(calc_rate('./Batch_4350992_batch_results.csv', './class_for_ds.tsv')) ## 48%
print(calc_rate('./Batch_4369243_batch_results.csv', './class_for_ds-1.tsv')) ## 57%
