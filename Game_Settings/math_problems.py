from random import choice

class Problems:

    def word_problem(self):
        problem_list = [
            '''On Monday, Johnny has 10 apples. Tuesday, he goes to the apple farm and picks up
            3 more. On Wednesday, he sells 6 to his friend Danny. Then on Thursday, he picks up
            another 2 apples. Today is Friday. How many apples does Johnny have?''',
            # On higher levels, add in oranges, and ask how many apples Danny has
            '''Nathaniel bought 3 shirts at the mall yesterday. Later on, he walked to the thrift
            store and picked up another shirt. By the end of the week, he gave 2 of his shirts to
            his brother Jaden. How many shirts does Nathaniel currently have?''',
            # For higher levels, separate into long sleeve and short sleeve,
            # and ask how many shirts his brother has
            '''Lisa walked 5 blocks north to the playground. She then walked 3 blocks east and
            1 block south to get to school. How many blocks in total did Lisa walk?''',
            # For higher levels, ask how many blocks in specific direction, or specific location
        ]

        return choice(problem_list)


    def permdas(self, *args):
        operations = ['+', '-', 'x', '/'] #Change to common division symbol
        prompt = ''
        # concatenate to prompt using iteration and args

        return prompt
