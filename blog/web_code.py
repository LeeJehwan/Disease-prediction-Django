import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
import os

rf = RandomForestClassifier(n_jobs=-1)
lgb_diab = LGBMClassifier(n_jobs=-1, )
rf_ab_rf = RandomForestClassifier(n_jobs=-1)
rf_hbp_lgbm = LGBMClassifier(n_jobs=-1)
rf_ab_lgbm = LGBMClassifier(n_jobs=-1)
rf_hbp = RandomForestClassifier(n_jobs=-1)


def train():
    PATH = os.getcwd()
    if PATH == '/home/LeeJehwan':
        PATH += '/my-first-blog'

    data_raw = pd.read_csv(PATH + '/data/dataset_to_web.csv')
    data = data_raw.copy()

    data_diab = data[['가입자일련번호','성별코드', '연령대코드(5세단위)', '허리둘레', '수축기혈압',
                      '이완기혈압','당뇨병 의사 판정','합병증_종류','BMI','구강검진 수검여부']]


    x_data = data_diab.drop(['합병증_종류',], axis = 1)
    y_data = data_diab['합병증_종류']

    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.3, random_state=42)

    x_test_id = x_test.reset_index(drop=True)
    x_train = x_train.drop('가입자일련번호', axis = 1)
    x_test = x_test.drop('가입자일련번호', axis = 1)


    # 1-1. Random Forest

    rf.fit(x_train, y_train)

    y_pred = rf.predict(x_test)

    # ### 1-2. LGBM(당뇨)
    #
    # lgb_diab.fit(x_train, y_train)
    #
    # ### 1-3. XGBoost(당뇨)
    #
    # xgb_diab.fit(x_train, y_train)
    # y_pred_diab_xgb = xgb_diab.predict(x_test)

    # 2. 고혈압만 환자들로 모델링

    ### 2-1. Random Forest

    data_hbp = data.copy()

    data_hbp=data[['가입자일련번호','성별코드',
                  '연령대코드(5세단위)', '허리둘레', '수축기혈압',
                  '이완기혈압','고혈압 의사 판정','합병증_종류','BMI','구강검진 수검여부']]
    x_data_hbp = data_hbp.drop(['합병증_종류',], axis = 1)
    y_data_hbp = data_hbp['합병증_종류']

    x_train_hbp, x_test_hbp, y_train_hbp, y_test_hbp = train_test_split(x_data_hbp, y_data_hbp,
                                                        test_size = 0.3, random_state=42)

    x_train_hbp = x_train_hbp.drop('가입자일련번호', axis = 1)
    x_test_hbp = x_test_hbp.drop('가입자일련번호', axis = 1)

    rf_hbp.fit(x_train_hbp, y_train_hbp)

    y_pred_hbp = rf_hbp.predict(x_test_hbp)

    ### 2-2. LGBM

    # data_hbp_lgbm = data.copy()
    #
    # data_hbp_lgbm=data[['가입자일련번호','성별코드',
    #               '연령대코드(5세단위)', '허리둘레', '수축기혈압',
    #               '이완기혈압','고혈압 의사 판정','합병증_종류','BMI','구강검진 수검여부']]
    #
    # x_data_hbp_lgbm = data_hbp_lgbm.drop(['합병증_종류',], axis = 1)
    # y_data_hbp_lgbm = data_hbp_lgbm['합병증_종류']
    #
    # x_train_hbp_lgbm, x_test_hbp_lgbm, y_train_hbp_lgbm, y_test_hbp_lgbm = train_test_split(x_data_hbp_lgbm, y_data_hbp_lgbm,
    #                                                     test_size = 0.3, random_state=42)
    #
    # x_train_hbp_lgbm = x_train_hbp_lgbm.drop('가입자일련번호', axis = 1)
    # x_test_hbp_lgbm = x_test_hbp_lgbm.drop('가입자일련번호', axis = 1)
    #
    # rf_hbp_lgbm.fit(x_train_hbp_lgbm, y_train_hbp_lgbm)
    #
    # y_pred_hbp_lgbm = rf_hbp_lgbm.predict(x_test_hbp_lgbm)

    ### 3. XGboost

    # data_hbp_xgb = data.copy()
    #
    # data_hbp_xgb=data[['가입자일련번호','성별코드',
    #               '연령대코드(5세단위)', '허리둘레', '수축기혈압',
    #               '이완기혈압','고혈압 의사 판정','합병증_종류','BMI','구강검진 수검여부']]
    #
    # x_data_hbp_xgb = data_hbp_xgb.drop(['합병증_종류',], axis = 1)
    # y_data_hbp_xgb = data_hbp_xgb['합병증_종류']
    #
    # x_train_hbp_xgb, x_test_hbp_xgb, y_train_hbp_xgb, y_test_hbp_xgb = train_test_split(x_data_hbp_xgb, y_data_hbp_xgb,
    #                                                     test_size = 0.3, random_state=42)
    #
    # x_train_hbp_xgb = x_train_hbp_xgb.drop('가입자일련번호', axis = 1)
    # x_test_hbp_xgb = x_test_hbp_xgb.drop('가입자일련번호', axis = 1)
    #
    # rf_hbp_xgb = XGBClassifier(n_jobs=-1, objective='multi:softprob')
    # rf_hbp_xgb.fit(x_train_hbp_xgb, y_train_hbp_xgb)
    #
    # y_pred_hbp_xgb = rf_hbp_xgb.predict(x_test_hbp_xgb)


    # 3. 이상지혈증 환자 모델

    ### 3- 1 RandomForest
    #
    # data_ab_rf = data.copy()
    #
    # data_ab_rf=data[['가입자일련번호','성별코드',
    #               '연령대코드(5세단위)', '허리둘레', '수축기혈압',
    #               '이완기혈압','지질혈증 의사 판정','합병증_종류','BMI','구강검진 수검여부']]
    #
    #
    # x_data_ab_rf = data_ab_rf.drop(['합병증_종류',], axis = 1)
    # y_data_ab_rf = data_ab_rf['합병증_종류']
    #
    # x_train_ab_rf, x_test_ab_rf, y_train_ab_rf, y_test_ab_rf = train_test_split(x_data_ab_rf, y_data_ab_rf,
    #                                                     test_size = 0.3, random_state=42)
    #
    # x_train_ab_rf = x_train_ab_rf.drop('가입자일련번호', axis = 1)
    # x_test_ab_rf = x_test_ab_rf.drop('가입자일련번호', axis = 1)
    #
    # rf_ab_rf.fit(x_train_ab_rf, y_train_ab_rf)
    #
    # y_pred_ab_rf = rf_ab_rf.predict(x_test_ab_rf)



    ### 3-2. LGBM

    data_ab_lgbm = data.copy()

    data_ab_lgbm=data[['가입자일련번호','성별코드',
                  '연령대코드(5세단위)', '허리둘레', '수축기혈압',
                  '이완기혈압','지질혈증 의사 판정','합병증_종류','BMI','구강검진 수검여부']]

    data_ab_lgbm['지질혈증 의사 판정'].value_counts()


    x_data_ab_lgbm = data_ab_lgbm.drop(['합병증_종류',], axis = 1)
    y_data_ab_lgbm = data_ab_lgbm['합병증_종류']

    x_train_ab_lgbm, x_test_ab_lgbm, y_train_ab_lgbm, y_test_ab_lgbm = train_test_split(x_data_ab_lgbm, y_data_ab_lgbm,
                                                        test_size = 0.3, random_state=42)

    x_train_ab_lgbm = x_train_ab_lgbm.drop('가입자일련번호', axis = 1)
    x_test_ab_lgbm = x_test_ab_lgbm.drop('가입자일련번호', axis = 1)

    rf_ab_lgbm.fit(x_train_ab_lgbm, y_train_ab_lgbm)

    y_pred_ab_lgbm = rf_ab_lgbm.predict(x_test_ab_lgbm)


    ### 3-3. Xgboost

    # data_ab_xgb = data.copy()
    #
    # data_ab_xgb=data[['가입자일련번호','성별코드',
    #               '연령대코드(5세단위)', '허리둘레', '수축기혈압',
    #               '이완기혈압','지질혈증 의사 판정','합병증_종류','BMI','구강검진 수검여부']]
    #
    # data_ab_xgb['지질혈증 의사 판정'].value_counts()
    #
    #
    # x_data_ab_xgb = data_ab_xgb.drop(['합병증_종류',], axis = 1)
    # y_data_ab_xgb = data_ab_xgb['합병증_종류']
    #
    # x_train_ab_xgb, x_test_ab_xgb, y_train_ab_xgb, y_test_ab_xgb = train_test_split(x_data_ab_xgb, y_data_ab_xgb,
    #                                                     test_size = 0.3, random_state=42)
    #
    # x_train_ab_xgb = x_train_ab_xgb.drop('가입자일련번호', axis = 1)
    # x_test_ab_xgb = x_test_ab_xgb.drop('가입자일련번호', axis = 1)
    #
    # rf_ab_xgb.fit(x_train_ab_xgb, y_train_ab_xgb)
    #
    # y_pred_ab_xgb = rf_ab_xgb.predict(x_test_ab_xgb)

def run_model(patient_type, test_data):
  if patient_type == '당뇨병':
      return disease_result(rf.predict(test_data))
  elif patient_type == '고혈압':
      return disease_result(rf_hbp.predict(test_data))
  elif patient_type == '이상지질혈증':
      return disease_result(rf_ab_lgbm.predict(test_data))


def disease_result(data):
    if data == 0 :
        return '합병증의 의심 여부가 없습니다.'
    elif data == 1:
        return '합병증(당뇨병 + 고혈압)이 예상됩니다.'
    elif data == 2:
        return '합병증(이상지질혈증 + 고혈압)이 예상됩니다.'
    elif data == 3:
        return '합병증(당뇨병 + 고혈압)이 예상됩니다.'
    elif data == 4:
        return '합병증(당뇨병 + 고혈압 + 이상지질혈증)이 예상됩니다.'