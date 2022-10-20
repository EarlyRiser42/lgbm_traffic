import pandas as pd
import category_encoders as ce
from haversine import haversine
import numpy as np

def in_jejudo():
    in_jeju_weekdays_2021 = [47445, 56835, 64137, 54879]
    in_jeju_weekend_2021 = [52111, 62606, 75889, 49812]
    in_west_weekdays_2021 = [46021, 54031, 62073, 56879]
    in_west_weekend_2021 = [47473, 54960, 68857, 46193]
    in_jeju_weekdays_2022 = [64930, 59757, 48707, 60278, 65030, 60952, 64688, 61254]
    in_jeju_weekend_2022 = [58055, 62785, 46007, 73909, 77201, 76137, 73186, 74487]
    in_west_weekdays_2022 = [62992, 56429, 48044, 58482, 62410, 61981, 62363, 56817]
    in_west_weekend_2022 = [60876, 56237, 43194, 67144, 68895, 67783, 65585, 65593]
    # 2021년
    for k in range(9, 13):
        # 평일
        train.loc[('제주시' == train['start_region_1']) & (train['month'] == k) &
                  (train['day'] <= 4) & (train['year'] == 2021), 'in_jeju_people'] = in_jeju_weekdays_2021[k-9]
        train.loc[('서귀포시' == train['start_region_1']) & (train['month'] == k) &
                  (train['day'] <= 4) & (train['year'] == 2021), 'in_west_people'] = in_west_weekdays_2021[k-9]
        # 주말
        train.loc[('제주시' == train['start_region_1']) & (train['month'] == k) &
                  (train['day'] > 4) & (train['year'] == 2021), 'in_jeju_people'] = in_jeju_weekend_2021[k-9]
        train.loc[('서귀포시' == train['start_region_1']) & (train['month'] == k) &
                  (train['day'] <= 4) & (train['year'] == 2021), 'in_west_people'] = in_west_weekend_2021[k-9]
    # 2022년
    for k2 in range(1, 9):
        # 평일
        train.loc[('제주시' == train['start_region_1']) & (train['month'] == k2) &
                  (train['day'] <= 4) & (train['year'] == 2022), 'in_jeju_people'] = in_jeju_weekdays_2022[k2 - 9]
        train.loc[('서귀포시' == train['start_region_1']) & (train['month'] == k2) &
                  (train['day'] <= 4) & (train['year'] == 2022), 'in_west_people'] = in_west_weekdays_2022[k2 - 9]
        # 주말
        train.loc[('제주시' == train['start_region_1']) & (train['month'] == k2) &
                  (train['day'] > 4) & (train['year'] == 2022), 'in_jeju_people'] = in_jeju_weekend_2022[k2 - 9]
        train.loc[('서귀포시' == train['start_region_1']) & (train['month'] == k2) &
                  (train['day'] <= 4) & (train['year'] == 2022), 'in_west_people'] = in_west_weekend_2022[k2 - 9]

def out_jejudo():
    out_jeju_weekdays_2021 = [51730, 60401,71218,62645]
    out_jeju_weekend_2021 = [56490,65312,79009,55512]
    out_west_weekdays_2021 = [44231,50254,59668,51095]
    out_west_weekend_2021 = [48527,57725,69804,46532]
    out_jeju_weekdays_2022 = [73431,67646,54145,66076,71756,71546,71219,63680]
    out_jeju_weekend_2022 = [68553,65952,53526,77318,81846,77837,77267,76093]
    out_west_weekdays_2022 = [59782,54032,45122,56657,61234,57317,61490,55516]
    out_west_weekend_2022 = [51558,56236,44477,70904,72832,70748,69365,68734]
    # 2021년
    for k in range(9, 13):
        # 평일
        train.loc[('제주시' == train['start_region_1']) & (train['month'] == k) &
                  (train['day'] <= 4) & (train['year'] == 2021), 'out_jeju_people'] = out_jeju_weekdays_2021[k-9]
        train.loc[('서귀포시' == train['start_region_1']) & (train['month'] == k) &
                  (train['day'] <= 4) & (train['year'] == 2021), 'out_west_people'] = out_west_weekdays_2021[k-9]
        # 주말
        train.loc[('제주시' == train['start_region_1']) & (train['month'] == k) &
                  (train['day'] > 4) & (train['year'] == 2021), 'out_jeju_people'] = out_jeju_weekend_2021[k-9]
        train.loc[('서귀포시' == train['start_region_1']) & (train['month'] == k) &
                  (train['day'] <= 4) & (train['year'] == 2021), 'out_west_people'] = out_west_weekend_2021[k-9]
    # 2022년
    for k2 in range(1, 9):
        # 평일
        train.loc[('제주시' == train['start_region_1']) & (train['month'] == k2) &
                  (train['day'] <= 4) & (train['year'] == 2022), 'out_jeju_people'] = out_jeju_weekdays_2022[k2 - 9]
        train.loc[('서귀포시' == train['start_region_1']) & (train['month'] == k2) &
                  (train['day'] <= 4) & (train['year'] == 2022), 'out_west_people'] = out_west_weekdays_2022[k2 - 9]
        # 주말
        train.loc[('제주시' == train['start_region_1']) & (train['month'] == k2) &
                  (train['day'] > 4) & (train['year'] == 2022), 'out_jeju_people'] = out_jeju_weekend_2022[k2 - 9]
        train.loc[('서귀포시' == train['start_region_1']) & (train['month'] == k2) &
                  (train['day'] <= 4) & (train['year'] == 2022), 'out_west_people'] = out_west_weekend_2022[k2 - 9]

def extract_year(row):
    return int(str(row)[0:4])

def extract_month(row):
    return int(str(row)[4:6])

def extract_day(row):
    return int(str(row)[6:])


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 600)

train = pd.read_parquet('../data/train.parquet')
test = pd.read_parquet('../data/test.parquet')

# Missing value handle
train.loc[(train['start_node_name'] == train['end_node_name']), 'road_name'] = train['start_node_name']
test.loc[(test['start_node_name'] == test['end_node_name']), 'road_name'] = test['start_node_name']

# Categorical to Numerical
for index, embark in enumerate(['월', '화', '수', '목', '금', '토', '일']):
    train.loc[(train['day_of_week'] == embark), 'day_of_week'] = index
    test.loc[(test['day_of_week'] == embark), 'day_of_week'] = index

for index, embark in enumerate(['없음', '있음']):
    train.loc[(train['start_turn_restricted'] == embark), 'start_turn_restricted'] = index
    test.loc[(test['start_turn_restricted'] == embark), 'start_turn_restricted'] = index
    train.loc[(train['end_turn_restricted'] == embark), 'end_turn_restricted'] = index
    test.loc[(test['end_turn_restricted'] == embark), 'end_turn_restricted'] = index

# Category Encoder
train['road_name'] = train['road_name'].replace('-', None)
test['road_name'] = test['road_name'].replace('-', None)

for name in ['road_name', 'start_node_name', 'end_node_name']:
    cat_encoder = ce.CatBoostEncoder(cols=[name], handle_missing='return_nan')
    train[name] = cat_encoder.fit_transform(train[name], train['target'])
    test[name] = cat_encoder.transform(test[name])

# separate base date to year, month, day
train['year'] = train['base_date'].apply(extract_year)
train['month'] = train['base_date'].apply(extract_month)
train['day'] = train['base_date'].apply(extract_day)
test['year'] = test['base_date'].apply(extract_year)
test['month'] = test['base_date'].apply(extract_month)
test['day'] = test['base_date'].apply(extract_day)

# add feature
train.loc[(train['maximum_speed_limit'] <= 40), 'road_types'] = 0  # 인접 도로
train.loc[(train['maximum_speed_limit'] == 50), 'road_types'] = 1  # 도심부 도로
train.loc[(train['maximum_speed_limit'] == 60) & (train['lane_count'] == 1), 'road_types'] = 2  # 도심부 외 도로
train.loc[(train['maximum_speed_limit'] == 60) & (train['lane_count'] >= 2), 'road_types'] = 1  # 도심부 도로
train.loc[(train['maximum_speed_limit'] > 60), 'road_types'] = 2  # 도심부 외 도로
train['road_types'] = train['road_types'].astype(dtype='int64')

test.loc[(train['maximum_speed_limit'] <= 40), 'road_types'] = 0  # 인접 도로
test.loc[(train['maximum_speed_limit'] == 50), 'road_types'] = 1  # 도심부 도로
test.loc[(train['maximum_speed_limit'] == 60) & (test['lane_count'] == 1), 'road_types'] = 2  # 도심부 외 도로
test.loc[(train['maximum_speed_limit'] == 60) & (test['lane_count'] >= 2), 'road_types'] = 1  # 도심부 도로
test.loc[(train['maximum_speed_limit'] > 60), 'road_types'] = 2  # 도심부 외 도로
test['road_types'] = test['road_types'].astype(dtype='int64')

# 성수기 비수기 추가(7월 23일~ 8월 5일)
train.loc[(7 == train['month']) & (train['day'] >= 23), 'peak_season'] = '1'
train.loc[(8 == train['month']) & (train['day'] <= 5), 'peak_season'] = '1'
train['peak_season'] = train['peak_season'].fillna(0)
train['peak_season'] = train['peak_season'].astype(dtype='int64')

test.loc[(7 == test['month']) & (test['day'] >= 23), 'peak_season'] = '1'
test.loc[(8 == test['month']) & (test['day'] <= 5), 'peak_season'] = '1'
test['peak_season'] = test['peak_season'].fillna(0)
test['peak_season'] = test['peak_season'].astype(dtype='int64')




# 도로 연장 추가
train['km'] = 0
test['km'] = 0
for haver in range(len(train)):
    start = ((train['start_latitude'][haver]), (train['start_longitude'][haver]))  # (lat, lon)
    goal = ((train['end_latitude'][haver]), (train['end_longitude'][haver]))  # (lat, lon)
    train['km'][haver] = haversine(start, goal)

for haver2 in range(len(test)):
    start = ((test['start_latitude'][haver2]), (test['start_longitude'][haver2]))  # (lat, lon)
    goal = ((test['end_latitude'][haver2]), (test['end_longitude'][haver2]))  # (lat, lon)
    test['km'][haver2] = haversine(start, goal)

# drop cols
train.drop(columns=['id', 'base_date', 'height_restricted', 'vehicle_restricted', 'multi_linked', 'connect_code', 'road_in_use'], inplace=True)
test.drop(columns=['id', 'base_date', 'height_restricted', 'vehicle_restricted', 'multi_linked', 'connect_code', 'road_in_use'], inplace=True)

print(train.head(50))
print('\n')
print(test.head(50))

# save processed dataset to parquet
train.to_parquet('../data/train_after.parquet', index=False)
test.to_parquet('../data/test_after.parquet', index=False)
