import math
import numpy as np
from State import State

#in this class we implement the function of f, h (the number of the visted, generated nodes)

class Puzzle:

    # Initializing the  Puzzle by the given (3) size, openSet and closedSet list
    # openSet = List of expanded states
    # closedSet = List of visited states

    def __init__(self, size):
        self.n = size
        self.openSet = []
        self.closedSet = []

        count = 0

    #store the input values in an array

    def values(self):
        create_matrix = []
        for i in range(0, self.n):
            store_value = input().split(",")
            create_matrix.append(store_value)
        return create_matrix

    #caluclating the f fun of the hamming

    def hamming_h(self, initial_state, goal_state):
        mis_tiles = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if initial_state[i][j] != goal_state[i][j] and initial_state[i][j] != '0':
                    mis_tiles += 1

        return mis_tiles


    #calcualting h fun of manhatten
    #cal the distance (space Complexity )

    def manhattan_h(self, initial_state, goal_state):
        manh_dist = []
        manhattan_dist = 0
        for i in range(0, 3):
            for j in range(0, 3):
                manh_dist.append(goal_state[i][j])

        for i in range(0, 3):
            for j in range(0, 3):
                current_coor = initial_state[i][j]
                x_coor = i
                y_coor = j
                index = manh_dist.index(current_coor)
                x_goal, y_goal = index // 3, index % 3
                if current_coor != '0':
                    manhattan_dist += (math.fabs(x_goal - x_coor) + math.fabs(y_goal - y_coor))

        return manhattan_dist

    #calcualting f fun of manhatten

    def manhattan_f(self, initial_state, goal_state):
        g_x = initial_state.level
        h_x = self.manhattan_h(initial_state.value, goal_state)
        f_x = g_x + h_x
        print("\ng(x): ", g_x)
        print("h(x): ", h_x)
        print("f(x): ", f_x)
        return f_x

    #calcualting f fun of hamming

    def misplace_f(self, initial_state, goal_state):
        g_x = initial_state.level
        h_x = self.hamming_h(initial_state.value, goal_state)
        f_x = g_x + h_x
        print("\ng(x): ", g_x)
        print("h(x): ", h_x)
        print("f(x): ", f_x)
        return f_x


        #copy of the main f function

    def f1(self, initial_state, goal_state):
        g_x = initial_state.level
        h_x = self.manhattan_h(initial_state.value, goal_state)
        f_x = g_x + h_x
        return f_x, g_x, h_x

    def main(self):
        counter = 0
        inv_count = 0


        print("\nInitial State \n")
        initial_state = self.values()
        print("\nGoal State \n")
        goal_state = self.values()
        print("\n Select the heuristic function h(x): \n1. Manhattan Distance \n2. Hamming Tiles ")
        choice = int(input())


        # testing if the intial state solveable or not

        a = np.array(initial_state)
        a[a == ''] = 0
        a = a.astype(np.integer)

        for i in range(0, 3):
            for j in range(0, 3):

                if 0 < a[i][j] < a[j][i]:
                    inv_count += 1

        print("inv: ", inv_count)

        if inv_count % 2 == 0:
            print("solveable CODE ")
            initial_state = State(initial_state, 0, 0)
            if choice == 1:
                initial_state.value_f = self.manhattan_f(initial_state, goal_state)
            else:
                initial_state.value_f = self.misplace_f(initial_state, goal_state)

            self.openSet.append(initial_state)
            print("\n\n")
            while True:

                cur = self.openSet[0]
                if counter == 0:
                    counter = 1
                else:
                    print("")
                    print("  |  ")
                    print("  |  ")
                    print(" \\/ \n")

                for i in cur.value:
                    for j in i:
                        print(j, end=" ")
                    print("")

                if choice == 1:
                    if self.manhattan_h(cur.value, goal_state) == 0:
                        break
                else:
                    if self.hamming_h(cur.value, goal_state) == 0:
                        break

                print(
                    "\n the values of f(x): ")
                for i in cur.generate_children():
                    if choice == 1:
                        i.value_f = self.manhattan_f(i, goal_state)
                    else:
                        i.value_f = self.misplace_f(i, goal_state)

                    self.openSet.append(i)

                self.closedSet.append(cur)
                del self.openSet[0]

                self.openSet.sort(key=lambda x: x.value_f, reverse=False)

            f, g, h = self.f1(cur, goal_state)
            print("\ng(x): ", g)
            print("h(x): ", h)
            print("f(x): ", f)
            print("Path Cost: ", f)
            print("Generated Nodes: ", len(self.openSet))
            print("Space Complexity (Expanded Nodes: ", len(self.closedSet))

        else:
            print(" not solvable CODE", )
            exit()
