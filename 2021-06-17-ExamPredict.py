# In this documentation I will be working with the test_scores.csv file. 

# The goal of this exercise is to train the train_df dataset and predict the value of posttest in the test_df dataset

# Observations:
1. There are 3 numerical values and 8 categorical, out of which 5 are binary(ish, as in 2 of them have 3 possible options to choose from), 1 variable is unique to each entry and 
    2 are names of schools and classrooms
Using the sns.FacetGrid I was able to determine a look at a variety of relationships between our goal feature ('posttest') and other features:
  1. The variable of school_setting has a large distribution difference between the 3 variables of urban suburban and rural
  2. School_type also
  3. Lunch
  4. pretest
  5. Teaching_method produced a unique shape where the mean value had the least examples
  6. Most schools have a sigma value of about 10 and low spread, witha  distinct characteristic to each school (eg. some behave poorly, others behave well.
