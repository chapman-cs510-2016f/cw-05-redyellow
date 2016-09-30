#!/usr/bin/env python3

from abscplane import AbsComplexPlane

class ComplexPlane(AbsComplexPlane):
	"""
	Abstract base class for complex plane.
	
	A complex plane is a 2x2 grid of complex numbers, having
	the form (x + y*1j), where 1j is the unit imaginary number in
	Python, and one can think of x and y as the coordinates for
	the horizontal axis and the vertical axis of the plane, 
	respectively. Recall that (1j)*(1j) == -1. Also recall that 
	the FOIL rule for multiplication still works:
	(x + y*1j)*(v + w*1j) = (x*v - y*w + (x*w + y*v)*1j)
	You can check these results in an interpreter.
	
	We will explore several implementations for a complex plane in
	this course, so we wish to have an abstract interface that
	is independent of any particular implementation.
	
	In addition to generating the 2x2 grid of numbers (x + y*1j),
	we wish to easily support transformations of the plane with
	an arbitrary function f. Done properly, the attribute self.plane
	should store a 2x2 grid of numbers f(x + y*1j) such that the
	parameter x ranges from self.xmin to self.xmax with self.xlen
	total points, while the parameter y ranges from self.ymin to
	self.ymax with self.ylen total points. By default, the function
	f should be the identity function id, which does nothing to
	the bare complex plane.
	
	Attributes:
	xmax (float) : maximum horizontal axis value
	xmin (float) : minimum horizontal axis value
	xlen (int)   : number of horizontal points
	ymax (float) : maximum vertical axis value
	ymin (float) : minimum vertical axis value
	ylen (int)   : number of vertical points
	plane        : stored complex plane implementation
	f    (func)  : function displayed in the plane
	"""
	def __init__(self, xmin, xmax, xlen, ymin, ymax, ylen):
		self.xmin = xmin
		self.xmax = xmax
		self.xlen = xlen
		self.ymin = ymin
		self.ymax = ymax
		self.ylen = ylen
		self.plane = []
		self.f=lambda x: x
	
	def refresh(self):
		"""
	Regenerate complex plane.
	For every point (x + y*1j) in self.plane, replace
	the point with the value self.f(x + y*1j). 
		"""
		self.plane = []
		for y in range(0, self.ylen):
			row = []
			for x in range(0, self.xlen):
				X=self.xmin+x
				Y=self.ymin+y
				row.append(self.f(X + Y*1j))
			self.plane.append(row)
		print(self.plane)

	def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
		"""
	Reset self.xmin, self.xmax, and/or self.xlen.
	Also reset self.ymin, self.ymax, and/or self.ylen.
	Zoom into the indicated range of the x- and y-axes.
	Refresh the plane as needed.
		"""
		self.xmin = xmin
		self.xmax = xmax
		self.xlen = xlen
		self.ymin = ymin
		self.ymax = ymax
		self.ylen = ylen
	
		self.refresh()
		

	def set_f(self,f):
		"""
	Reset the transformation function f.
	Refresh the plane as needed.
		"""
		self.f = f
		self.refresh()
		return 0
'''
Test
p1=ComplexPlane(0,3,4,0,2,3)
p1.refresh()
p1.zoom(1,2,2,0,3,4)
p1.set_f(lambda x:x+2)
p1.zoom(1,2,2,1,3,3)
'''
