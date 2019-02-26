# Bite 105. Slice and dice

Take the block of text provided and `strip` off the whitespace at both ends. Split the text by newline (\n) using `split`.

Loop through the lines and if the first character of each (stripped) line is lowercase, split the line into words and add the last word to the (given) `results` list, stripping the trailing dot (.) and exclamation mark (!) from the end of the word.

At the end of the function return the `results` list.