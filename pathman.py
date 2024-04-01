import os
import sys
import shutil

home = os.path.expanduser('~')
pathman_dir = os.path.join(home, '.pathman')
pathman_file = os.path.join(pathman_dir, '.config')

def setup() -> None:
    if not os.path.exists(pathman_dir):
        os.mkdir(pathman_dir)

    if not os.path.exists(pathman_file):
        with open(pathman_file, 'w') as new:
            new.write('# NANANANA PATHMAN!\n')
            new.write('alias pathman=\'python3 ' + pathman_dir + '/pathman.py\'\n')

            print('Dotfile created at {}.'.format(pathman_file))
            print('Add \'source ~/.pathman/.config\' to .bashrc or .zshrc')

        shutil.move(
                os.path.join(os.getcwd(), 'pathman.py'),
                os.path.join(pathman_dir, 'pathman.py')
        )


def make_binary_alias(bin_path : str, alias : str) -> None:
    if (os.path.exists(bin_path)):
        abs_path = os.path.abspath(bin_path)
        with open(pathman_file, 'a') as config:
            config.write('alias {}=\'{}\'\n'.format(alias, abs_path))

        print('Aliased \'{}\' to {}, added to .pathman file.'.format(alias, abs_path))
    else:
        print('Check file location: {}'.format(bin_path))


def make_command_alias(command_text : str, alias : str) -> None:
    # command must use absolute path, or have all components in $PATH
    with open(pathman_file, 'a') as config:
        config.write('alias {}=\'{}\'\n'.format(alias, command_text))

    print('Aliased \'{}\' to {}, added to .pathman file.'.format(alias, command_text))
        

def remove_alias(name : str) -> None:
    lines = ''
    with open(pathman_file, 'r') as old:
        lines = old.readlines()

    removed = False
    with open(pathman_file, 'w') as new:
        for line in lines:
            if (line.startswith(name, 6)): # offset of name is 6 chars in
                print('\'{}\' was removed from .pathman file.'.format(name))
                removed = True
                continue;

            new.write(line)
    
    if not removed:
        print('\'{}\' was not found in the .pathman file, check spelling.\n'.format(name))
        list_aliases()


def list_aliases() -> None:
    with open(pathman_file, 'r') as config:
        for line in config.readlines():
            print(line)


if __name__ == '__main__':
    
    arg_len = len(sys.argv)
    setup()

    if (arg_len == 4 and sys.argv[1] == '--a'):
        make_binary_alias(sys.argv[2], sys.argv[3])

    elif (arg_len == 4 and sys.argv[1] == '--c'):
        make_command_alias(sys.argv[2], sys.argv[3])

    elif (arg_len == 3 and sys.argv[1] == '--r'):
        remove_alias(sys.argv[2])

    elif (arg_len == 2 and sys.argv[1] == '--l'):
        list_aliases()

    else:
        print((
            'Usage:\n' 
            '--a <filename : str> <alias : str> : Alias source binary without arguments\n'
            '--c <command : str> <alias : str> : Alias command/binary with arguments\n'
            '--l : List aliases in .pathman file\n'
            '--r <alias_name : str> : Remove aliases from .pathman file\n'
        ))

