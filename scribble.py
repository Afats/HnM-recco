transactions = transactions.drop_duplicates(subset=['customer_id','article_id'])
transactions= transactions.reset_index(drop = True)
customer_list = transactions.customer_id.value_counts()[:50].index.tolist()
customers_1 = customers.loc[customers['customer_id'].isin(customer_list)]
transactions_t = transactions.loc[transactions['customer_id'].isin(customer_list)]
articles_t = articles.loc[articles['article_id'].isin(list(transactions_t['article_id']))]
merge_df = pd.DataFrame()
for customer in customers_1['customer_id']:
    new_df = pd.DataFrame()
    new_df['Buy'] = []
    print(customer)
    new_df = new_df.append([customers_1.loc[customers_1['customer_id']==customer]]*len(articles_t)).reset_index(drop = True)
    new_df['article_id'] = list(articles_t['article_id'])
    tran_temp = transactions_t.loc[transactions_t['customer_id']==customer]
    for article in list(tran_temp['article_id']):
        new_df.loc[(new_df['customer_id']==customer) & (new_df['article_id']==article),['Buy']] = 1
    merge_df = merge_df.append(new_df).reset_index(drop = True)
merge_df