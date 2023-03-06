# 0x06. Regular expression <code>*Regex*</code> <code>*DevOps*</code>
 By: Bernard B. Sakyi
 

## Concepts
*For this project, I looked at this concept:*

* [Regular Expression](https://intranet.alxswe.com/concepts/29)


## Background Context
For this project, I had to build my regular expression using Oniguruma, a regular expression library that is used by Ruby by default. 

NB: Other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

<code>
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
</code>

## Resources
#### Read or watch:

* Regular expressions - basics
* Regular expressions - advanced
* Rubular is your best friend
* Use a regular expression against a problem: now you have 2 problems
* Learn Regular Expressions with simple, interactive exercises

## Requirements
### General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 20.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby
* All your regex must be built for the Oniguruma library

## Tasks
* *Mandatory Tasks:*
   * [0-simply_match_school.rb](0-simply_match_school.rb)
   * [1-repetition_token_0.rb](1-repetition_token_0.rb)
   * [2-repetition_token_1.rb](2-repetition_token_1.rb)
   * [3-repetition_token_2.rb](3-repetition_token_2.rb)
   * [4-repetition_token_3.rb](4-repetition_token_3.rb)
   * [5-beginning_and_end.rb](5-beginning_and_end.rb)
   * [6-phone_number.rb](6-phone_number.rb)
   * [7-OMG_WHY_ARE_YOU_SHOUTING.rb](7-OMG_WHY_ARE_YOU_SHOUTING.rb)


