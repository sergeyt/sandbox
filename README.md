# sandbox

Sandbox to

- Practise git commands
- Try out markdown syntax
- Host misc small scripts

## Work with git remote branches

### Creating a Remote Branch

1. Create the remote branch

    git push origin origin:refs/heads/new_feature_name

2. Make sure everything is up-to-date

    git fetch origin

3. Then you can see that the branch is created.

    git branch -r

4. Start tracking the new branch

    git checkout --track -b new_feature_name origin/new_feature_name

5. Make sure everything is up-to-date

    git pull

### Cleaning up Mistakes

If you make a mistake you can always delete the remote branch

    git push origin :heads/new_feature_name

### Use the Branch from Another Location

When you get to another computer or clone the git repository to a new computer, then you just need to start tracking the new branch again.

    git branch -r

to show all the remote branches

    git checkout --track -b new_branch origin/new_feature_name

to start tracking the new branch.

## markdown cheat sheet

([source](http://warpedvisions.org/projects/markdown-cheat-sheet/))

A short sheet of the Markdown syntax. See the the complete [Markdown
syntax](http://daringfireball.net/projects/markdown/syntax) for extra tasty
details.

    # Header 1 #
    ## Header 2 ##
    ### Header 3 ###             (Hashes on right are optional)
    #### Header 4 ####
    ##### Header 5 #####
    
    ## Markdown plus h2 with a custom ID ##         {#id-goes-here}
    [Link back to H2](#id-goes-here)
    
    This is a paragraph, which is text surrounded by whitespace. Paragraphs can
    be on one line (or many), and can drone on for hours.
    
    Here is a Markdown link to [Warped](http://warpedvisions.org), and a literal .
    Now some SimpleLinks, like one to [google] (automagically links to are-you-
    feeling-lucky), a [wiki: test] link to a Wikipedia page, and a link to
    [foldoc: CPU]s at foldoc.
    
    Now some inline markup like _italics_,  **bold**, and `code()`. Note that
    underscores in words are ignored in Markdown Extra.
    
    ![picture alt](/images/photo.jpeg "Title is optional")
    
    > Blockquotes are like quoted text in email replies
    >> And, they can be nested
    
    * Bullet lists are easy too
    - Another one
    + Another one
    
    1. A numbered list
    2. Which is numbered
    3. With periods and a space
    
    And now some code:
    
        // Code is just text indented a bit
        which(is_easy) to_remember();
    
    ~~~
    
    // Markdown extra adds un-indented code blocks too
    
    if (this_is_more_code == true && !indented) {
        // tild wrapped code blocks, also not indented
    }
    
    ~~~
    
    Text with
    two trailing spaces
    (on the right)
    can be used
    for things like poems
    
    ### Horizontal rules
    
    * * * *
    ****
    --------------------------
    
    
    <div class="custom-class" markdown="1">
    This is a div wrapping some Markdown plus.  Without the DIV attribute, it
    ignores the block.
    </div>
    
    ## Markdown plus tables ##
    
    | Header | Header | Right  |
    | ------ | ------ | -----: |
    |  Cell  |  Cell  |   $10  |
    |  Cell  |  Cell  |   $20  |
    
    * Outer pipes on tables are optional
    * Colon used for alignment (right versus left)
    
    ## Markdown plus definition lists ##
    
    Bottled water
    : $ 1.25
    : $ 1.55 (Large)
    
    Milk
    Pop
    : $ 1.75
    
    * Multiple definitions and terms are possible
    * Definitions can include multiple paragraphs too
    
    *[ABBR]: Markdown plus abbreviations (produces an <abbr> tag)
