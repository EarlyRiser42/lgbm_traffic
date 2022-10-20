import pandas as pd
from catboost import Pool, CatBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import optuna
from optuna.samplers import TPESampler


def objective(trial):
    train = pd.read_parquet('data/train_cat.parquet')
    y = train['target']
    x = train.drop(columns=['target'])

    x_2, x_test, y_2, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    x_train, x_val, y_train, y_val = train_test_split(x_2, y_2, test_size=0.12, random_state=42)
    train_pool = Pool(x_train,
                      y_train,
                      cat_features=['day_of_week', 'road_name', 'road_rating', 'connect_code', 'road_type',
                                    'start_node_name',
                                    'start_turn_restricted', 'end_node_name', 'end_turn_restricted'])
    val_pool = Pool(x_val,
                      y_val,
                      cat_features=['day_of_week', 'road_name', 'road_rating', 'connect_code', 'road_type',
                                    'start_node_name',
                                    'start_turn_restricted', 'end_node_name', 'end_turn_restricted'])
    test_pool = Pool(x_test,
                     cat_features=['day_of_week', 'road_name', 'road_rating', 'connect_code', 'road_type',
                                   'start_node_name',
                                   'start_turn_restricted', 'end_node_name', 'end_turn_restricted'])
    param = {}
    param['random_state'] = 42
    param['eval_metric'] = 'RMSE'
    param['task_type'] = 'GPU'
    param['iterations'] = 2000
    param['learning_rate'] = 0.1
    param['depth'] = trial.suggest_int('depth', 4, 15)
    param['l2_leaf_reg'] = trial.suggest_float('l2_leaf_reg', 2, 10)
    param['min_child_samples'] = trial.suggest_int('min_data_in_leaf', 1, 50)
    param['random_strength'] = trial.suggest_float('random_strength', 0, 10)

    regressor = CatBoostRegressor(**param)
    regressor.fit(train_pool, eval_set=[val_pool], early_stopping_rounds=20)
    loss = mean_absolute_error(y_test, regressor.predict(test_pool))
    return loss


if __name__ == "__main__":
    sampler = TPESampler(seed=42)
    study = optuna.create_study(direction="minimize", sampler=sampler)
    study.optimize(objective, n_trials=10)

    print("Number of finished trials: {}".format(len(study.trials)))

    print("Best trial:")
    trial = study.best_trial

    print("  Value: {}".format(trial.value))

    print("  Params: ")
    for key, value in trial.params.items():
        print("    {}: {}".format(key, value))

