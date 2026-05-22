# -*- coding: utf-8 -*-
"""
Created on Fri May 22 23:12:44 2026

@author: Karan Raj
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 16:16:14 2019

@author: Karan Raj
"""




item_similarity = sklearn.metrics.pairwise.cosine_similarity(nor_sparse)
user_similarity = sklearn.metrics.pairwise.cosine_similarity(nor_sparse.T)

item_sim_df = pd.DataFrame(item_similarity, index = nor.index, columns = nor.index)
user_sim_df = pd.DataFrame(user_similarity, index = nor.columns, columns = nor.columns)


def similar_user_recs(user):
    
    if user not in nor.columns:
        return('No data available on user {}'.format(user))
    
    sim_users = user_sim_df.sort_values(by=user, ascending=False)
    best = []
    most_common = {}
    
    for i in sim_users:
        max_score = nor.loc[:, i].max()
        best.append(nor[nor.loc[:, i]==max_score].index.tolist())
    for i in range(len(best)):
        for j in best[i]:
            if j in most_common:
                most_common[j] += 1
            else:
                most_common[j] = 1
    sorted_list = sorted(most_common.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_list[:200]    

def predicted_quantity(item_code, user):
    sim_users = user_sim_df.sort_values(by=user, ascending=False)
   # print(len(sim_users))
    user_values = user_sim_df.sort_values(by=user, ascending=False).loc[:,user].tolist()
    quantity_list = []
    weight_list = []
    for j, i in enumerate(sim_users):
        quantity = Inv_index.loc[i,item_code]
        similarity = user_values[j]
        if np.isnan(quantity):
            continue
        elif not np.isnan(quantity):
            quantity_list.append(quantity*similarity)
            weight_list.append(similarity)
    return np.round(sum(quantity_list)/sum(weight_list))
#len(similar_user_recs(27270)) 
predicted_quantity("22633V",127269)
pred=[]
i=0

for user in test.CustomerID.unique():
    u=[]
    for item in test.StockCode.unique():
           
        if (predicted_quantity(item,user)>0):
                u.append(item)
    pred.append(u)
    i=i+1
    print(i)
pd.DataFrame(test.CustomerID.unique())



with open('D:\PGDBA\Comp\IBM/csvfile.csv','a') as file:
    file.write('CustomerID,Items')
    file.write('\n')
    for user in test.CustomerID.unique():
        file.write(str(user))
        #file.write(",['")
        p=preds_df.loc[user].dropna(how='any').index
        pfd=pd.DataFrame(data=str(p))
        
        #file.write(str(p).lstrip('(').rstrip(')'))
        #file.write(str(p))
        #file.write("']")
        
        file.write('\n')
