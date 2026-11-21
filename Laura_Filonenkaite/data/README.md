1) eats table with columns: hour, food, glucose 
2) checks glucose level during every eating (base); detects spike
3) makes table: food, base, peak, spike

4) duration of the spike --> when glucose came back, measure how long it took for glucoze to stabilise
5) plot day glucose graph; 

6) make code with food
7) make code for few days

8) make possible opperation to plot only needed day
9) modules:
        - file path as a variable of the function
        - make function to return sth (not to print), because i want to use data
        - if function saves sth - saving name as variable (new data - new name)

correct the tables (units, days)
draw two graphs for vegetable comparison table
make clear window for user (to leave modules in another file)
make tables for serious cases (60) and mid(30); 
detect foods that make highest influence



UNIVERSAL TAKING FILE FROM ANOTHER SUBFOLDER:


data_dir = Path(__file__).resolve().parent.parent / "data":
csv_file = data_dir / "trial_3d.csv"

data_dir                  - encoded direction
Path(__file__).resolve()  - takes path of THIS file
.parent                   - comes back by 1 folder
"data"                    - Points into the "data" subfolder (next to user and raw)
csv_file = ...            - Point to the particular file 