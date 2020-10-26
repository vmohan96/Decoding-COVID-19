ideas:

* show an interactive graph of up to all 50 states which compare the rise in covid vs the calculated mask sentiment up to june 2020

* after june, plot a fitted curve vs estimated covid mask sentiment and the actual points

* use the values for mask sentiment in june as coefficents for an equation which predicts current covid metrics from january to june

* then introduce a slider which can change all 50 mask coefficents

* equation will look like this:

\\[\LARGE f(t)=C_1F_1t_1+C_2F_2t_2+...+C_nF_nt_n\\]

Where C is the covid mask sentiment bewteen 0 and 1, F is a fitting factor and t is the time, represented as days since day 0 of data collection 

This equation assumes that the covid mask sentiment in each state remains consistent over a period of 6 months. One of my major assumptions is that the mask sentiment from January to days before the survey is cointained within the survey data because we have found an association with mask sentiment and political alignment.

F can be understood as a multiplying factor which is the impact of covid on a given state with a given mask sentiment. I chose the factors to be multipilicative because the spread of covid can be understood as a exponential factory where one person can potentially infect an infinte amount of people within a 2 week window, as understood by up to date CDC research.

We can separate this linear equation into a system of linear equations as understood by matrix A where:



Implementations:

Plot the points on a plot, then plot on top various equations to fit ot the data

Run points through a log regression to fit a curve




flask deployment:

have a slider which changes mask sentiment past june 2020 to show changes in the curve

show the equation produced in latex