# In this documentation I will be working with the test_scores.csv file. 

# The goal of this exercise is to train the train_df dataset and predict the value of posttest in the test_df dataset

# Observations:
1. There are 3 numerical values and 8 categorical, out of which 5 are binary(ish, as in 2 of them have 3 possible options to choose from), 1 variable is unique to each entry and 
    2 are names of schools and classrooms

Using the sns.FacetGrid & .groupby determine relationships between our goal feature ('posttest') and other features:
  1. The variable of school_setting has a large distribution difference between the 3 variables of urban suburban and rural, with urban mean: 61.7, rural is 64 and suburban is 76.
  2. School_type also (64.0 for public, 75.9 for non-public)
  3. Lunch
  4. pretest
  5. Teaching_method: mean: S-63, E-73
  6. Most schools have a sigma value of about 10 and low spread, witha  distinct characteristic to each school (eg. some behave poorly, others behave well.
  7. num_students doesn't have a clear pattern at first sight, further observation is needed
  https://github.com/RusskiBoyVlad/test-repository/issues/1#issue-924245356
  
  
Conversion of categorical into numerical values:
    Converted var into num
    
Things to do:
    1. Check for outliers
    2. Run a variety of algorithms in order to compare their performances
    3. run a nn
    4. XGBooost

