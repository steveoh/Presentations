# Docopt

1. Documents your command-line application
1. Generates a parser for your command line application

### Command Line Applications

1. Multiple sub-commands exist in one application
1. Map inputs to dictionary keys. Input order is not important

### Syntax

`<positional_argument>`: `my_program <input1> <input2>`

`-o --option`: these two options are identical
 - short option syntax can be stacked: `-abc`
 - long option values can use a space or an equal sign: `--name output.txt` == `--name=output.txt`
 - short options can use a space or no space: `-n output.txt` == -noutput.txt
 
`[options arguments or commands within square brackets are optional]`: `my_program [command] [--option] [<argument>]`
 - you can also combine the example into `my_program [command --option <argument>]`
  
`(options or arguments within round brackets are required)`
**All elements are required by default if not included in `[]`**  
in this instance if you provide `<one-argument>` you will also need to provide `<another_argument>`: `my_program [(<one-argument> <another-argument>)]` 

### Install

`pip install docopt`
