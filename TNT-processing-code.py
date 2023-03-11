#22 Jul 2021
# Code written by Usman Afzali with extensive help from Abdullah Naeem
## Use of this code: post-experimental data processing of TNT experiment
## package needed: pandas. you may also need to pip install openpyxl if you are using PyCharm.

#importing the needed package. pandas should already be installed on your machine.
import pandas as pd

#read the excel sheet after it's been uploaded to this python file's location.
#a sample Excel sheet (sample.xlsx) is provided in this repository.

df = pd.read_excel(r'folder location from computer\sample.xlsx', sheet_name='Sheet1')

#get the index of the SP and IP columns so they can be read by the code
sp_index = df.columns.get_loc('SP')
ip_index = df.columns.get_loc('IP')

crit = df.iloc[71:137, ip_index + 1]
crit_response = df.iloc[71:137, ip_index + 2]

#drop grey rows = filler/practice pairs
crit1 = crit.drop(71)
crit2 = crit1.drop(72)
crit4 = crit2.drop(77)
crit5 = crit4.drop(83)
crit6 = crit5.drop(87)
crit7 = crit6.drop(89)
crit8 = crit7.drop(95)
crit9 = crit8.drop(96)
crit10 = crit9.drop(103)
crit11 = crit10.drop(104)
crit12 = crit11.drop(111)
crit13 = crit12.drop(112)
crit14 = crit13.drop(117)
crit15 = crit14.drop(120)
crit16 = crit15.drop(125)
crit17 = crit16.drop(130)
crit18 = crit17.drop(135)
crit_f = crit18.drop(136)
crit_response1 = crit_response.drop(71)
crit_response2 = crit_response1.drop(72)
crit_response4 = crit_response2.drop(77)
crit_response5 = crit_response4.drop(83)
crit_response6 = crit_response5.drop(87)
crit_response7 = crit_response6.drop(89)
crit_response8 = crit_response7.drop(95)
crit_response9 = crit_response8.drop(96)
crit_response10 = crit_response9.drop(103)
crit_response11 = crit_response10.drop(104)
crit_response12 = crit_response11.drop(111)
crit_response13 = crit_response12.drop(112)
crit_response14 = crit_response13.drop(117)
crit_response15 = crit_response14.drop(120)
crit_response16 = crit_response15.drop(125)
crit_response17 = crit_response16.drop(130)
crit_response18 = crit_response17.drop(135)
crit_response_f = crit_response18.drop(136)


#Makes series data for the SP and IP dataset.
cr_data = pd.Series([1 if response == 1 else 0 for response in crit_response_f],
                         index = crit_f)



#get all three needed columns and change them together to a dataframe

SP_data = pd.Series([1 if response == 1 else 0 for response in df.iloc[:48, sp_index+ 2]],
                         index = df.iloc[:48, sp_index+1])

IP_data = pd.Series([1 if response == 1 else 0 for response in df.iloc[:48, ip_index+ 2]],
                         index = df.iloc[:48, ip_index+1] )

#Converts all data into one dataframe.
CR_SP_IP = pd.DataFrame({'criterion': cr_data, 'SP': SP_data, 'IP':IP_data})


#introduce counterbalance pattern for A = T, NT, and BL. For B, it will be TN, BL, and T.
## for C, it is BL, T, and NT.

think_A = ['UNCLE',
'ROACH',
'LAMB',
'DOLL',
'CIGAR',
'LEMON',
'BLUE',
'NECKLACE',
'JAR',
'HOUSE',
'BOURBON',
'SWORD',
'STEEL',
'NORTH',
'GRANITE',
'GOLDFISH']

no_think_A = ['TOASTER',
'FALCON',
'CARBON',
'PHYSICS',
'VALLEY',
'DAISY',
'SADNESS',
'CHEDDAR',
'PENNY',
'BALLET',
'COTTON',
'FLUTE',
'LOBSTER',
'NUTMEG',
'PHANTOM',
'ROBBERY']

baseline_A = ['HOUR',
'CLOWN',
'CHAIR',
'SNOW',
'BICYCLE',
'TOMATO',
'SULFUR',
'SHIRT',
'HAMMER',
'POODLE',
'SANDAL',
'TOMB',
'COBRA',
'FOOTBALL',
'OAK',
'PICTURE']

think_A_df = CR_SP_IP
no_think_A_df = CR_SP_IP
baseline_A_df = CR_SP_IP

for word, row in CR_SP_IP.iterrows():

    if word not in think_A:
        think_A_df = think_A_df.drop(word)
    if word not in no_think_A:
        no_think_A_df = no_think_A_df.drop(word)
    if word not in baseline_A:
        baseline_A_df = baseline_A_df.drop(word)


# a = learned and recalled.
## b = not learned and recalled.
### c = learned and not recalled.
#### d = a + b
        
def answer_a_b_c_d(df, name):
    count_dict = {}

    count_dict['count_a_sp'] = 0
    count_dict['count_a_ip'] = 0
    count_dict['count_b_sp'] = 0
    count_dict['count_b_ip'] = 0
    count_dict['count_c_sp'] = 0
    count_dict['count_c_ip'] = 0
    count_dict['count_d_sp'] = 0
    count_dict['count_d_ip'] = 0

    count_a_sp = 0
    count_a_ip = 0

    count_b_sp = 0
    count_b_ip = 0

    count_c_sp = 0
    count_c_ip = 0

    count_c = 0
    count_d = 0

    for word, row in df.iterrows():
        if row['criterion'] == 1 and row['SP'] == 1:
            count_a_sp += 1
            count_dict['count_a_sp'] = count_a_sp

        if row['criterion'] == 1 and row['IP'] == 1:
            count_a_ip += 1
            count_dict['count_a_ip'] = count_a_ip

        if row['criterion'] == 1 and row['SP'] == 0:
            count_b_sp += 1
            count_dict['count_b_sp'] = count_b_sp

        if row['criterion'] == 1 and row['IP'] == 0:
            count_b_ip += 1
            count_dict['count_b_ip'] = count_b_ip

        if row['criterion'] == 0 and row['SP'] == 1:
            count_c_sp += 1
            count_dict['count_c_sp'] = count_c_sp

        if row['criterion'] == 0 and row['IP'] == 1:
            count_c_ip += 1
            count_dict['count_c_ip'] = count_c_ip

    count_d_sp = count_a_sp + count_c_sp
    count_d_ip = count_a_ip + count_c_ip

    crit_count_one = df['criterion'].sum()

    unconditionalised_recall_sp = ((count_d_sp) / 16) * 100
    conditionalised_recall_sp = ((count_d_sp) / crit_count_one) * 100

    unconditionalised_recall_ip = ((count_d_ip) / 16) * 100
    conditionalised_recall_ip = ((count_d_ip) / crit_count_one) * 100

    count_dict['count_' + name] = crit_count_one

    count_dict['count_d_sp'] = count_d_sp
    count_dict['count_d_ip'] = count_d_ip

    count_dict['unconditionalised_recall_sp'] = unconditionalised_recall_sp
    count_dict['conditionalised_recall_sp'] = conditionalised_recall_sp

    count_dict['unconditionalised_recall_ip'] = unconditionalised_recall_ip
    count_dict['conditionalised_recall_ip'] = conditionalised_recall_ip

    count_series = pd.Series(count_dict, name=name)

    return count_series

results_think = answer_a_b_c_d(think_A_df, 'THINK')
results_no_think = answer_a_b_c_d(no_think_A_df, 'NO-THINK')
results_baseline = answer_a_b_c_d(baseline_A_df, 'Baseline')


print(results_think)
print(results_no_think)
print(results_baseline)
