#
#		Michael Cooper
#		Ohio University CS 3560
#		Project 6
#


puts "Enter String\n"
contents = gets

contents = contents.gsub(/(?<!^\A|^\s)f(?![^a-z^A-Z])/, '\2gh')

#replace i in middle of words
contents = contents.gsub(/\Bi(?!\s)/, '\1o') 		#(?!match) negative lookahead assertion; matches, but does not include the match when changing text

contents = contents.gsub(/(?<![^a-z^A-Z]|\A)sh(?<!\s)/, '\2ti')


print contents