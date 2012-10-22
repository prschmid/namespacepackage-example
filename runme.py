#!/usr/bin/python

# Add the two packages to the path
import sys
sys.path.append('project1')
sys.path.append('project2')

# Import the modules from the two packages
import mypackage.module1
import mypackage.module2
import mypackage.module3

if __name__ == '__main__':
	# Create some objects from the first package
	p1_foo = mypackage.module1.foo.Foo()
	p1_bar = mypackage.module1.bar.Bar()
	p1_SomeClass = mypackage.module2.SomeClass()

	# Create some objects from the second package
	p2_bar = mypackage.module3.bar.Bar()
	p2_baz = mypackage.module3.baz.Baz()

	# Show that they all work
	p1_foo.run_me()
	p1_bar.run_me()
	p1_SomeClass.run_me()

	p2_bar.run_me()
	p2_baz.run_me()
