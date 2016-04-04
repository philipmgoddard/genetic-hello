#set term post eps color enhanced
#set output 'plot.eps'

set term pngcairo size 700, 400
set output 'plot.png'

set rmargin 10

set logscale y
set xlabel 'Iteration'
set ylabel 'Cost'
set key off

set xrange [0:1600]
set yrange [0.5:100000]

# assumes iteration number is in col 1 and cost in col 2
plot 'results.txt' u 1:2 w l lt rgb '#5296D4' lw 2
