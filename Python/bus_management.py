import calendar
import random
import os

EACH_TYPE_OF_SEATS = 30

AC = []
for i in range(EACH_TYPE_OF_SEATS):
    AC.append(f'AC{i+1}')
NON_AC = []
for i in range(EACH_TYPE_OF_SEATS):
    NON_AC.append(f'NAC{i+1}')
Sleeper = []
for i in range(EACH_TYPE_OF_SEATS):
    Sleeper.append(f'S{i+1}')


class Bus:
    def __init__(self, from_place, to_place, date_of_journey, no_of_passengers, type_of_ticket):
        self.busses = {
            1: {
                'AC': AC
            },
            2: {
                'NON_AC': NON_AC
            },
            3: {
                'SLEEPER': Sleeper
            }
        }
        self.AC_cost = 500
        self.NON_AC_cost = 300
        self.SLEEPER_cost = 400
        self.AC_timings = ['09:45', '15:00']
        self.NON_AC_timings = ['11:15', '18:45']
        self.SLEEPER_timings = ['13:30', '20:30']
        self.from_place = from_place
        self.to_place = to_place
        self.date = date_of_journey
        self.no_passengers = no_of_passengers
        self.ticket_type = type_of_ticket
        print('___________________________________________________')
        print('                   | M E N U |                     ')
        print('                   -----------                     ')
        print('Total number of busses: 3')
        print('Total number of tickets: 90')
        print('Bus-1    AC Bus: 30 seats')
        print('Bus-2    NON_AC Bus: 30 seats')
        print('Bus-3    SLEEPER Bus: 30 seats')
        print('Cost   AC: Rs.500, NON_AC: Rs.300, SLEEPER: Rs.400')
        print('___________________________________________________')

    def seat_availability(self):
        if self.ticket_type == 'AC':
            if len(self.busses[1]['AC']) >= self.no_passengers:
                print(f"BUS NO. {1} is available", end=', ')
                print(f"Available AC seats: {len(self.busses[1]['AC'])}")
                print(f"AC bus available at {self.AC_timings} IST.")
                print(f"Amount per AC seat: Rs.{self.AC_cost}")
            else:
                print(f"Insufficient seats in BUS NO. {1}.")
        elif self.ticket_type == 'NON_AC':
            if len(self.busses[2]['NON_AC']) >= self.no_passengers:
                print(f"BUS NO. {2} is available", end=', ')
                print(f"Available NON_AC seats: {len(self.busses[2]['NON_AC'])}")
                print(f"NON_AC bus available at {self.NON_AC_timings} IST.")
                print(f"Amount per NON_AC seat: Rs.{self.NON_AC_cost}")
            else:
                print(f"Insufficient seats in BUS NO. {2}.")
        elif self.ticket_type == 'SLEEPER':
            if len(self.busses[3]['SLEEPER']) >= self.no_passengers:
                print(f"BUS NO. {3} is available", end=', ')
                print(f"Available SLEEPER seats: {len(self.busses[3]['SLEEPER'])}")
                print(f"SLEEPER bus available at {self.SLEEPER_timings} IST.")
                print(f"Amount per SLEEPER seat: Rs.{self.SLEEPER_cost}")
            else:
                print(f"Insufficient seats in BUS NO. {3}.")

    def reservation(self, selection_of_seats, card_num, cvv):
        if self.ticket_type == 'AC':
            bus_timings = self.AC_timings
            bus_selection = 1
            print("Since you choose AC ticket, BUS NO. 1 selected.\n")
        elif self.ticket_type == 'NON_AC':
            bus_timings = self.NON_AC_timings
            bus_selection = 2
            print("Since you choose NON_AC ticket, BUS NO. 2 selected.\n")
        else:
            bus_timings = self.SLEEPER_timings
            bus_selection = 3
            print("Since you choose SLEEPER ticket, BUS NO. 3 selected.\n")
        self.date = list(map(str, self.date))
        bus_date = '-'.join(self.date)
        print(f"Congratulations! You have successfully booked {self.no_passengers} seats from {self.from_place} "
              f"to {self.to_place}, at {random.choice(bus_timings)} IST, on {bus_date}.\n")
        for seat in range(selection_of_seats):
            seat_no = self.busses[bus_selection][f'{self.ticket_type}'].pop()
            print(f"Selected seat: {seat_no}", end=', ')
            print(f"Seat selected in row: {len(self.busses[bus_selection][f'{self.ticket_type}'])+1}\n")

        if card_num and cvv:
            num_of_tickets = selection_of_seats
            if self.ticket_type == 'AC':
                cost_per_ticket = self.AC_cost
            elif self.ticket_type == 'NON_AC':
                cost_per_ticket = self.NON_AC_cost
            else:
                cost_per_ticket = self.SLEEPER_cost
            total_cost = num_of_tickets*cost_per_ticket
            if dict_weekday[weekday] == 'Sat' or dict_weekday[weekday] == 'Sun':
                print("Since you are booking tickets on weekend, you have to pay 10% extra on ticket price:-\n")
                print(f"Total amount : Rs.{round(1.1 * total_cost, 2)}\n")
            else:
                print(f"Total amount : Rs.{total_cost}\n")


from_ = input('From where do you want to travel: ')
to_ = input('Enter destination: ')
no_of_tickets = int(input('How many passengers: '))
date = input("Enter the date (DD MM YYYY): ").split()
date = list(map(int, date))
weekday = calendar.weekday(date[2], date[1], date[0])
dict_weekday = {
    0: 'Mon',
    1: 'Tue',
    2: 'Wed',
    3: 'Thu',
    4: 'Fri',
    5: 'Sat',
    6: 'Sun'
}
ticket_type = input('Select ticket type [AC, NON_AC, SLEEPER]: ').upper()
os.system('cls')
my_bus = Bus(from_place=from_, to_place=to_, date_of_journey=date, no_of_passengers=no_of_tickets,
             type_of_ticket=ticket_type)
print('\n')
input('Press any key to continue: ')
os.system('cls')
my_bus.seat_availability()
print('\n')
input('Press any key to continue: ')
os.system('cls')
acc_num = int(input('Enter your bank account number: '))
cvv_num = int(input("Enter your cvv: "))
os.system('cls')
my_bus.reservation(selection_of_seats=no_of_tickets, card_num=acc_num, cvv=cvv_num)
