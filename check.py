

def paste_string(data, name, num_start, num_end):
    string = ''
    for i in range(num_start, num_end + 1):
        if data[name + str(i)] != '-':
            string = string + data[name + str(i)] + ' '
    item = string.split(sep=' ')
    # item = list(set(item))
    item.remove('')
    return item

def check_relation(list_company, list_investor):
    r = 0
    for i in list_company:
        for j in list_investor:
            if (i in j) | (j in i):
                r += 1
    return r

def check_percent(string_company, string_investor):
    list_investor = string_investor.split(sep=' ')
    percent = list_investor.count(string_company) / len(list_investor)
    return percent

def check_competitor(string_company, string_investor, data = data_itjuzi):
    list_investor = str(string_investor).split(sep=' ')
    count = 0
    check = 0
    for i in list_investor:
        if not data['二级分类'][data['项目名'] == i].empty:
            if (data['二级分类'][data['项目名'] == i] == string_company).bool():
                count += 1
    if count > 0:
        check = 1
    return [check, count]

# ok 尚未考虑级别 #    工作经历 * 投资人工作经历
# ok 尚未考虑级别 #    教育经历 * 投资人教育经历
# ok #    一级分类 * 投资组合行业 （比重）
# 暂不考虑 #     获投金额（币种） * 投资组合金额（币种）（比重）
# ok 但尚未分大类 #     获投轮次 * 投资组合轮次（比重）
# #     投资人投资项目
# ok 仅做了二级分类竞品 #     项目名 * 投资组合名称（竞品分析）
# 未完成，需要匹配 #    一级地区 or 二级地区 * 机构总部

# 原信息模型 + 基金模型 + 人际关系模型

check_relation(paste_string(data_itjuzi.iloc[1], '工作经历', 1, 12), paste_string(data_invjuzi.iloc[1], '投资人工作经历', 1, 60))
check_relation(paste_string(data_itjuzi.iloc[1], '教育经历', 1, 12), paste_string(data_invjuzi.iloc[1], '投资人教育经历', 1, 60))
check_percent(data_itjuzi['一级分类'].iloc[4], data_invjuzi['投资组合行业'].iloc[1])
check_percent(data_itjuzi['项目名后轮次'].iloc[4], data_invjuzi['已投资轮次'].iloc[1])
check_competitor(data_itjuzi['二级分类'].iloc[4], data_invjuzi['投资组合名称'].iloc[1])

# --------------------- End ----------------------


string_company=data_itjuzi['二级分类'].iloc[4]
string_investor=data_invjuzi['投资组合名称'].iloc[1]



if ((not data['二级分类'][data['项目名'] == 'Sigtuple'].empty) & \
        (data['二级分类'][data['项目名'] == 'Sigtuple'] == string_company).bool()):
    count += 1

if not data_itjuzi['二级分类'][data_itjuzi['项目名'] == '999'].empty:
    print('found')
data_invjuzi['投资组合名称'].apply(lambda x: str(x).split(sep=' '))
data_itjuzi['一级分类'].value_counts()
data_itjuzi['二级分类']

paste_string(data_itjuzi.iloc[1], '创业经历', 1, 12)
paste_string(data_itjuzi.iloc[15], '工作经历', 1, 12)
paste_string(data_itjuzi.iloc[1], '教育经历', 1, 12)
paste_string(data_invjuzi.iloc[25], '投资人工作经历', 1, 60)
paste_string(data_invjuzi.iloc[1], '投资人教育经历', 1, 60)
paste_string(data_invjuzi.iloc[1], '投资组合行业', 1, 60)





data_itjuzi['工作经历1'] data_invjuzi['投资人工作经历1'] # 工作经历直接dummy?  bubububu, 要跟投资机构的工作经历比对
data_itjuzi['教育经历1'] data_invjuzi['投资人教育经历1'] # 比对

data_invjuzi['投资组合行业']  # 行业占以前的比重      # 需要一个比对字符计数的函数
data_invjuzi['投资组合金额']　# 当前币种，占曾经被投资的比重，
                               # 目标金额和历史平均的差别
投资组合轮次
data_invjuzi['投资组合轮次'] #　当前投资轮次占历史的百分之几

data_invjuzi['投资人职位1'] # 暂时没有给职位赋权重
data_invjuzi['投资人投资项目1']
# 项目所在地 * 投资机构所在地
