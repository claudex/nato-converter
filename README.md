# NATO Phonetic Alphabet Converter

Convert list of character to the equivalent in NATO alphabet and digits in ITU/IMO alphabet. And it takes care
of the capitals:

	$ ./nato_converter.py aBc
	aBc: alpha BRAVO charlie

This is useful to give password orally and avoid confusion:

	$ ./nato_converter.py $( pwgen 8 1)
	Mahngi8i: MIKE alpha hotel november golf india Oktoeight india

If you don't specify an argument, it reads stdin:

	$ pwgen 3 2 | ./nato_converter.py
    Ym20Ge: YANKEE mike Bissotwo Nadazero GOLF echo

