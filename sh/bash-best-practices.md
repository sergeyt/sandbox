# Bash Best Practices

@ymattw

Table Of Contents

- Why, when and when not
- Common sense
- Variable
- Here document
- Wildcards
- Quoting
- Tests
- Functions
- Exit code
- Redirecting and piping
- Compound expressions
- Trapping
- Debugging
- Standard tools
- References

## Why, when and when not

### Why shell scripting

Shell scripting is the most efficient way to

- Use existing powerful Unix commands and tools
- Build apps by gluing together commands, tools and compiled binaries

### Why bash

- Linux standard
- Still growing (in favor of ksh etc.)

### When shell scripting

- Rule of thumb: do things like a "shell" (i.e. wrapper)

### When not to use shell scripts

- Speed (performance) is a factor
- Extensive file operations required (lseek, flock, etc.)
- Need complex data structures
- Need direct access to system hardware
- Need socket I/O
- Too many arbitrary precision calculation

## Common sense

### Know your environment

- $PATH
- Working dir
- Current user
- Compatibility

### Follow a coding style

- Naming convention
- Text width
- Indent
- Commenting
- No hardcoding

### Organize your source tree

    .                               .
    |-- run.sh                      |-- bin/
    |-- report.sh                   |   |-- run.sh
    |-- utils.sh           ----\    |   `-- report.sh
    |-- testconfig.sample  ----/    |-- lib/
    `-- logs/                       |   |-- liblog.sh
                                    |   |-- libutil.sh
                                    |   |-- libreport.sh
                                    |   |-- libmail.sh
                                    |   `-- libssh.sh
                                    |-- conf/
                                    |   `-- testconfig.sample
                                    `-- logs/

Bad habit (left side)
: Is your utils.sh too long?

Good habit (right side)
: Organize by functionality as modules

### Name space?

Sorry, no name space available.  Instead, use functions with good a naming
convention.

- Choose global names carefully, uppercased, (consider move into a main() function)
- Use "local" modifier for all function scope variables, lowercased

    Y_HOME=/home/y
    Y_CONF=$Y_HOME/conf
    
    function ssh_setup()
    {
        local host=${1?}
        local output
        ...

### Naming convention

Bad style: too common, likely to conflict

    DEBUG_LVL=0
    ...
    function error()
    ...
    function dump_variables()
    ...
    function setup_ssh()

Good style: **prefix** is your buddy

    # In liblog.sh
    LOG_LEVEL=0
    function log_error()
    
    # In libutil.sh
    function util_dump_variables()
    
    # In libssh.sh
    function ssh_setup()


## Variable

### Variable assignment

    FOO=foo                             # No spaces around the equal
    FOO="$FOO bar"                      # FOO now is "foo bar"
    FOO+=" bar"                         # Requires bash 3.2+
    read -p "Enter your name: " NAME    # read from stdin

### Variable expansion

    FOO=$BAR                            # Or FOO=${BAR}
    FOO=${BAR}_COUNT                    # Now {} is mandatory
    NAME=$(id -u)                       # Sub shell expansion
    OUTPUT=$(myfunc)                    # Note extracts stdout only
    TMP=~/tmp                           # Expands to "$HOME/tmp"
    TMP=~user/tmp                       # Expands to user's $HOME/tmp

### Indirect Variable Reference

Use evaludation

    KEYWORD_US="ipad"
    KEYWORD_FR="café"
    for market in "US" "FR"; do
        eval "KEYWORD=\\$KEYWORD_${market}"
        echo "Keyword for $market is $KEYWORD"
    done

We get:

    Keyword for US is ipad
    Keyword for FR is café

For market "US", the expression after "eval" command first expanded to

    eval "KEYWORD=$KEYWORD_US"

Then evaluated as

    KEYWORD=ipad

### Special variables

$0, $1, ..., $9, ${10}, ...
: Positonal variables

$$
: Current shell pid, won't change in sub shells
: e.g: tmpfile="/tmp/.inputdata.$$"

$!
: pid of the most recent background job

$?
: Exit code of **most recent** expression
:
:    parse_config $config
:    if (( $? != 0 )); then
:        err_quit "Failed to parse $config (rc=$?)"  # oops!
:    fi

NOTE: "export" is for child processes, not subshells

## Here document

Variables expands in here document

    cat << EOF
    Usage:
        $0 –a <adserver> -b <broker>
    Example:
        $0 –a $(hostname) –b $DEFAULT_SERVER
    EOF

Avoid expanding in here document

- cat &lt;&lt; \\EOF
- cat &lt;&lt; "EOF"

## Wildcards

Wildcard is handy

- \*, ?, [a-z], /path/to/{foo,bar\*}.conf

But be aware

- ssh $remotehost ls /home/y/logs/\*.log
- \*.log will be expanded locally!
- Solution: use quotes

Watch out, especially when use with "rm"!

"rm" is dangerous, review before press ENTER!

>   Date: Wed, 10 Jan 90
>   From: djones@megatest.uucp (Dave Jones)
>   Subject: rm *
>   Newsgroups: alt.folklore.computers2
>
>   Anybody else ever intend to type:
>
>     % rm *.o
>
>   And type this by accident:
>
>     % rm *>o
>
>   Now you've got one new empty file called "o", but plenty of room for it!

[Page 21 "The Unix-haters Handbook"]

Another example:

    rm –rf $SERVRE_LOG_DIR/*

Oops, I am root! Painful, huh?

Good habit saves you:

    rm –rf ${SERVER_LOG_DIR:?}/*

Your get a "parameter null or not set" error if variable name was misspelled.

Side notes:

- Don't run as root as possible as you can
- Drop root privilege once you don't need anymore

## Quoting
## Tests
## Functions
## Exit code
## Redirecting and piping
## Compound expressions
## Trapping
## Debugging
## Standard tools
## References

