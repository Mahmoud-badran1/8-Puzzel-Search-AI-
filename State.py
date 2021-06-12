
class State:

  #we need the value we got to generate the children nodes
  #Level is to caluculate the


    def __init__(self, value, level, value_f):
        self.value = value
        self.level = level
        self.value_f = value_f

    #the function automate the moves of the specific element(zero), in all cases when the edge is not viseable then remove this chance and so on.

    def generate_children(self):
        x, y = self.search_space(self.value, '0')
        # The Direction
        coor_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in coor_list:
            child = self.valid_position(self.value, x, y, i[0], i[1])
            if child is not None:
                child_node = State(child, self.level + 1, 0)
                children.append(child_node)

        return children

    # Function searches for the position of zero

    def search_space(self, puz, x):
        for i in range(0, len(self.value)):
            for j in range(0, len(self.value)):
                if puz[i][j] == x:
                    return i, j


    #is the valid postion valid for ZERO
    #this fun checks the valid postion of ZERO

    def valid_position(self, puz, x1, y1, x2, y2):

        if 0 <= x2 < len(self.value) and 0 <= y2 < len(self.value):
            temp_puz = self.copy_matrix(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

   #copy of the given matrix

    def copy_matrix(self, root):

        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp
