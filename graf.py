import pylab as pl 
from numpy import pi


f = 50

t = pl.linspace(0, 0.1, 333)

u = 3.3 * pl.cos(2*pi*f*t)
i = 1.1 * pl.cos(2*pi*f*t+pi/4)

p = u * i

pl.figure(1)
pl.plot(t, u, 'g*',  label='u(t)', color='#abcdef')
pl.plot(t, i, 'b*', label='i(t)', linestyle=':', linewidth=6)
pl.plot(t, p, 'r', label='p(t) = u(t) * i(t)')
pl.grid(True)
pl.legend(loc='upper right')

pl.xlim([0, 0.04])
pl.title('Výkon střídavého proudu.')
pl.xlabel('t [s]')
pl.ylabel('u(t), i(t), p(t)')



pl.show()