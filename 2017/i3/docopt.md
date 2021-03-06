# Docopt
> docopt does one thing and does it well: it implements your command-line interface.

There is no validation other than the command-line interface. For data validation docopt recommends [schema](https://github.com/keleshev/schema)

[Prereq blog post reading](https://gis.utah.gov/the-evolution-of-a-python-script/)

### Why

1. Documents your command-line application
1. Generates a parser for your command line application

### About

- https://github.com/docopt
  - implemented in many languages
  - https://github.com/docopt/docopt
- http://try.docopt.org/

### Command Line Applications

1. Multiple sub-commands exist in one application
1. Map inputs to dictionary keys. Input order is not important

### Syntax

###### Sub Commands
Anything that is not in a `<>`, `[]`, `()`, or following a `-` or `--`

```
Usage: my_program_file.py FILE
       my_program_file.py COUNT FILE
```

###### Arguments
`<positional_argument>`: `my_program <input1> <input2>`

```
Usage: my_program_file.py FILE <input1>
       my_program_file.py COUNT FILE <input1>
```

###### Options
`-o --option`: these two options are identical
 - short option syntax can be stacked: `-abc`
 - long option values can use a space or an equal sign: `--name output.txt` == `--name=output.txt`
   - I recommend being in the habbit of using the equal sign as there are caveats when omitted
 - short options can use a space or no space: `-n output.txt` == `-noutput.txt`
   - i recommend being in the habbit of using the space as there are caveats when omitted
   
When doc'ing your options:
1. they must start with a `-`
1. use two spaces after to add the description
1. you can set default values by adding a `[default: <the-default-value>]` at the end of the description
```
Options:
  --verbose
  -o FILE  the output file [default: ./]
  -o FILE --output=FILE  the long and short version of ouput    ### With arguments without comma, with "=" sign
  -i <file>, --input <file>
Other: --bad  # BAD, line does not start with dash "-"
```
   
If you have a lot of options that are all applicatble you can use the `[options]` shortcut
```
my_program [options] <path>

--all             List everything.
--long            Long output.
--human-readable  Display in human-readable format.
```
instead of
```
my_program [--all --long --human-readable] <path>

--all             List everything.
--long            Long output.
--human-readable  Display in human-readable format.
```

###### Optional vs Required
`[options arguments or commands within square brackets are optional]`: `my_program [command] [--option] [<argument>]`
 - you can also combine the example into `my_program [command --option <argument>]`
  
`(options or arguments within round brackets are required)`
**All elements are required by default if not included in `[]`**

in this instance if you provide `<one-argument>` you will also need to provide `<another_argument>`: `my_program [(<one-argument> <another-argument>)]` 

###### This or That
Mutually exclusive (choose one) can be created with the `|` pipe operator: `my_program go (--up | --down | --left | --right)`
 
 - in the example you **have** to choose only one option
 
`my_program go [--up | --down | --left | --right]`

 - in this example you **could** choose only one option

```
my_program run [--fast]
my_program jump [--high]
```

could be written as
```my_program (run [--fast] | jump [--high])```

Choose whatever makes more sense to you for readability

###### One or more
`element...` allows for repeating items one or more times  

the parsed dictionary will contain an array of items that were split by a space



### Install

`pip install docopt`


### Usage

```
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__)
```
