set terminal png size 800,300 enhanced
set output 'resonanceplot.png'

f(x) = 1./(x*x)
g(x) = 3./(x*x + 3.)

set multiplot layout 1,2 rowsfirst

set xrange [-10:10]

set yrange [0:1.3]

unset key

plot f(x) with lines lt rgb "black" lw 4


set arrow from -1.6,0.5 to 1.6,0.5 heads size 0.5,45 front ls 201 lt rgb "red" lw 3

plot g(x) with lines lt rgb "black" lw 4

unset multiplot

