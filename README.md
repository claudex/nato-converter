#Nato converter

Convert list of character to the equivalent in NATO alphabet. And it takes care
of the capitals:

	$ ./nato_converter.py abc
	aBc: alpha BRAVO charlie

This is useful to give password orally and avoid confusion:

	$ ./nato_converter.py $( pwgen 8 1)
	Mahngi8i: MIKE alpha hotel november golf india 8 india

If you don't specify an argument, it reads stdint:

	$ pwgen 3 2 | ./nato_converter.py
	Ym2 0Ge : YANKEE mike 2  0 GOLF echo 


