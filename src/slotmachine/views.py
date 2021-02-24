from django.views import View
from django.http import HttpResponse
from django.template import loader
from random import choices
# import numpy
# from time import sleep

credit = 10

class JackPotView(View):
    def get(self, request, action=''):
        # print(action)

        template = loader.get_template('slotmachine/home.html')
        context = {}
        # C = CHERRY
        # L = LEMON
        # O = ORANGE
        # W = WATERMELON
        fruits = {
            'C': 10,
            'L': 20,
            'O': 30,
            'W': 40
        }

        if action == 'play':
            output = []
            for i in range(0, 3):
                output.append(choices(list(fruits.keys()))[0])

            template = loader.get_template('slotmachine/jackpot.html')
            global credit

            if self.win(output):
                credit += fruits[output[0]]
                #result = f'You win {fruits[output[0]]} credits'
            else:
                # result = 'You lose'
                credit -= 1

            # print(credit)

            context = {
                'output': output,
                'credit': credit,
                #'result': result,
                'you_can_play': self.you_can_play(),
            }
            return HttpResponse(template.render(context, request))

        elif action == 'cash_out':
            credit = 10
            template = loader.get_template('slotmachine/home.html')
            return HttpResponse(template.render(context, request))

        return HttpResponse(template.render(context, request))

    def win(self, iterable):
        if iterable[0] == iterable[1] == iterable[2]:
            return True
        else:
            # print('Return false')
            return False

    def you_can_play(self):
        global credit
        if credit <= 0:
            return False
        else:
            return True

    def restart_credit(self):
        global credit
        credit = 10