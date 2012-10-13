class Data:

    def __init__(self, char, weight):
        self.char = char
        self.weight = weight

    def __str__(self):
        return '''<'%s', %d>''' % (self.char, self.weight)

    def __cmp__(self, other):
        return self.weight - other.weight


class Tree:

    def __init__(self, data, parent, lchild, rchild):
        self.data = data
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild

    def __str__(self):
        return '''<data='%s', parent='%s', lchild='%s', rchild='%s'>''' % \
                (self.data, self.parent, self.lchild, self.rchild)


class Huffman:

    def __init__(self, data_seq):
        self.data_seq = data_seq

    def huffman(self):
        forest = []
        for d in self.data_seq:
            forest.append(Tree(d, None, None, None))

        while len(forest) > 1:
            forest.sort(key=lambda tree: tree.data)
            weight = forest[0].data.weight + forest[1].data.weight
            new_data = Data('', weight)
            new_node = Tree(new_data, None, forest[0], forest[1])
            forest[0].parent = new_node
            forest[1].parent = new_node

            # new tree append to list so that it appears right side if another
            # tree has the same weight
            #
            forest.append(new_node)
            forest.pop(0)
            forest.pop(0)
        return forest[0]

    def print_all(self, root):
        # NOTE: root is a complete tree, so lchild is None means rchild is None
        # too
        #
        if root.lchild:
            self.print_all(root.lchild)
            self.print_all(root.rchild)
        else:
            code = []
            x = root
            while x.parent is not None:
                if x.parent.lchild is x:
                    code.insert(0, '0')
                else:
                    code.insert(0, '1')
                x = x.parent
            code.insert(0, root.data.char + ': ')
            print ''.join(code)


if __name__ == '__main__':
    '''The huffman coding will work like this:

    1. sort to (3 5 7 8 11 14 23 29)
    2. choose (3 5) to form a new tree with weight 8 and replace (3 5)
       in the list
           7 8 11 14 23 29  8  
                           3 5 
    3. resort to
           7   8   8   11 14 23 29
                  3 5
    4. repeat
            8   11  14    15     23 29
           3 5           7  8 
    5.
          14    15        19     23 29
               7  8     8   11 
                       3 5     
    6.
              19     23 29     29      
            8   11          14    15   
           3 5                   7  8  
    7.                                 
            29     29                42      
                14    15        19      23   
                     7  8     8   11         
                             3 5             
    8.
                     42          58           
                19      23    29     29       
              8   11              14    15    
             3 5                       7  8   
    9.
                           100
                     42          58           
                19      23    29     29       
              8   11              14    15    
             3 5                       7  8   
    '''

    data_seq = []
    data_seq.append(Data('A', 5))   # expect 0001
    data_seq.append(Data('B', 29))  # expect 10
    data_seq.append(Data('C', 7))   # expect 1110
    data_seq.append(Data('D', 8))   # expect 1111
    data_seq.append(Data('E', 14))  # expect 110
    data_seq.append(Data('F', 23))  # expect 01
    data_seq.append(Data('G', 3))   # expect 0000
    data_seq.append(Data('H', 11))  # expect 001

    h = Huffman(data_seq)
    root = h.huffman()
    h.print_all(root)

# EOF
