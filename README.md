# pathman
Personal Linux alias manager (Use at own risk)

```
Usage:
--a <filename : str> <alias : str> : Alias source binary without arguments
--c <command : str> <alias : str> : Alias command/binary with arguments
--l : List aliases in .pathman file
--r <alias_name : str> : Remove aliases from .pathman file
```

Note: if you want to use a command like: `sudo some-alias`, you will need to add 
`alias sudo='sudo '` to your `.zshrc/.bashrc` file. This is due to 
[how bash aliases work](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Aliases).
