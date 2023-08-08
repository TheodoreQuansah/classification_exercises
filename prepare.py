def prep_iris(get_iris_data):

    return iris_df

def prep_titanic(get_titanic_data):

    return titanic_df

def prep_telco(get_telco_data):

    return telco_df

def train_val_test(df, strat, seed = 42):

    train, val_test = train_test_split(df, train_size = 0.7, random_state = seed, stratify = df[strat])

    val, test = train_test_split(val_test, train_size = 0.5, random_state = seed, stratify = val_test[strat])

    return train, val, test