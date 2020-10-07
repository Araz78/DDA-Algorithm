from bokeh.plotting import figure, output_file, show
#=========================================== input x1,x2 y1,y2 values
x1 = int(input("Please Enter Value of x1: "))
y1 = int(input("Please Enter Value of y1: "))
x2 = int(input("Please Enter Value of x2: "))
y2 = int(input("Please Enter Value of y2: "))
#=========================================== Calculate the value of m
Delta_y = y2 - y1
Delta_x = x2 - x1
m = abs(float(Delta_y / Delta_x))
#=========================================== Insert the values ​​of x,y
if m < 1:
    X_k = [xk for xk in range(x1 , x2+1)]
    len_X_k = len(X_k)

    Y_k = []
    first = float(y1)
    Y_k.append(first)
    w = first
    for i in range(0 , len_X_k):
        w = float(w) + float(m)
        w_round = round(w)
        Y_k.append(w_round)

else :
    Y_k = [yk for yk in range(y1 , y2+1)]
    len_Y_k = len(Y_k)

    X_k = []
    first = float(x1)
    X_k.append(first)
    w = first
    for i in range(0 , len_Y_k):
        w = float(w) + float(1 / m)
        w_round = round(w)
        X_k.append(w_round) 
#=========================================== Draw lines
output_file("DDA lines.html")

p = figure(title="DDA Algorithm", x_axis_label='x', y_axis_label='y')
p.line(X_k, Y_k, legend_label="Temp.", line_width=5)
show(p)
# Araz Alinejad