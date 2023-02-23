for col_name in df_num_removed.columns:
    df_num_removed[col_name] = df_num_removed[col_name].str.split('.', 1).str[1]
    df_num_removed[col_name] = df_num_removed[col_name].str[1:]