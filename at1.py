from turtle import *
color ("Blue",  "Black")
begin_fill()
while true:
	forward(200)
	left(170)
	if abs(pos()) <1:
		break
end_fill()
done()
