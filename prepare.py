def clean_weapons(df):
    '''This function cleans the weapons dataframe.'''
    # make all columns lowercase
    df.columns = df.columns.str.lower()
    # replace nulls with non-upgradeable
    df.loc[df['upgrade'].isnull(), 'upgrade'] = 'non-upgradeable'
    # drop perk and speed columns
    df.drop(['perk', 'speed'], axis=1, inplace=True)
    return df