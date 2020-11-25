#!/usr/bin/env python3


class DonorData:
    """
    Class stores donor data as an object
    """

    def __init__(self, name):
        self.donations = []
        self.name = name

    def add_donation(self, *args):
        """
        Used to add multiple donations to the donations property
        :param args: must be decimal or int
        :return: None
        """
        for num in args:
            self.donations.append(num)


class MenuController:
    """
    Class centralizes controls for front-end menu texts
    """

    def __init__(self):
        self._text_selector = {'main': 'Please make a selection\n1. Send a Thank You Letter\n2. Create Report\n3. Write'
                                       ' letters to file\n4. Exit',
                               'donor_select': 'Type List to see donors. To select donor, type donors name. '
                                               'If donor does not exist, type name to create new donor',
                               'donation_amount': 'Please enter donation amount. '
                                                  'Enter multiple amounts separated by spaces.',
                               'num_error': 'Please enter a number!',
                               }

    def return_text(self, key):
        """
        returns value by key
        :param key: str
        :return: str
        """
        return self._text_selector.get(key)


class ProgramController:
    """
    Class centralizes controls for the application
    """

    def __init__(self, donors_list):
        self.user_input = None
        self.exit = False
        self.donors = donors_list

    def list_or_add_donor(self, input_command):
        """
        Returns a list of donors if the command is list, otherwise it will add a new donor
        :param input_command: str
        :return: List, None
        """
        if input_command == 'list':
            return self.donors
        else:
            new_donor = DonorData(input_command)
            self.donors.append(new_donor)

    def select_donor(self, input_name):
        """
        Returns donor object in list of donors
        :param input_name: str
        :return: DonorData
        """
        if len(self.donors) > 0:
            for i in range(len(self.donors)):
                if self.donors[i].name == input_name:
                    return self.donors[i]
            return None

    def thank_you_letter(self, name):
        """
        Personalizes a thank you letter to donor
        :param name: str
        :return: str
        """
        letter = f'Aloha {name}!\nWe here at the Mailroom LLC wish to give you mad props for sending a much needed' \
                 ' donation. We welcome your kindness, and again, a big mahalo to you from the MailRoom!'
        return letter

    def create_report(self):
        """
        Creates a report of donor activity
        :return: str
        """
        print('Donor Name' + ' ' * 10 + '|' + 'Total Given' + ' ' * 10 + '|' + 'Num Gifts' + ' ' * 10 + '|'
              + 'Average Gift' + '\n'
              + '-' * ((15 * 4) + len('Donor Name') + len('Total Given') + len('Num Gifts') + 4))
        for don in self.donors:
            print('{:<15} {:>15} {:>15} {:>15}'.format(don.name, sum(don.donations), len(don.donations),
                                                       sum(don.donations) / len(don.donations)))

    def write_letter_to_file(self):
        """
        write letter to file
        :return: None
        """
        # get names from donor list
        names = [obj.name for obj in self.donors]

        # create file using name
        for name in names:
            outfile = open(f'{name}.txt', 'w')
            outfile.write(self.thank_you_letter(name))
            outfile.close()


# create test donors

donor1 = DonorData('Scott Guyton')
donor2 = DonorData('James Brown')
donor3 = DonorData('Spicy Chicken')
donor4 = DonorData('Potato Pizza')
donor5 = DonorData('Hip Hop Cop')
donor_list = [donor1, donor2, donor3, donor4, donor5]

# add values to donations
for x in donor_list:
    x.add_donation(150, 3000, 900000)

# init controller
controller = ProgramController(donor_list)
menu = MenuController()

if __name__ == '__main__':
    while controller.exit is False:
        controller.user_input = input(str(menu.return_text('main')))
        if controller.user_input == '4':
            controller.exit = True
        elif controller.user_input == '1':
            controller.user_input = input(menu.return_text('donor_select'))
            # check for name in list first
            if controller.select_donor(controller.user_input):
                selection = controller.select_donor(controller.user_input)
                donation_amount = input(menu.return_text('donation_amount'))
                input_list = donation_amount.split(' ')
                try:
                    convert_to_int = [int(x) for x in input_list]
                    selection.donations.add_donations(convert_to_int)
                except ValueError:
                    print(menu.return_text('num_error'))

                # send out letter
                print(controller.thank_you_letter(selection.name))
                continue
            else:
                # check for list or name not found
                list_or_new = controller.list_or_add_donor(controller.user_input)
                if list_or_new:
                    for donor_obj in list_or_new:
                        print(f'Name:{donor_obj.name} Donations:{donor_obj.donations}\n')
                    continue
                else:
                    selection = controller.select_donor(controller.user_input)
                    donation_amount = input(menu.return_text('donor_select'))
                    input_list = donation_amount.split(' ')
                    try:
                        convert_to_int = [int(x) for x in input_list]
                        selection.donations.add_donations(convert_to_int)
                    except ValueError:
                        print(menu.return_text('num_error'))

                    # send out letter
                    print(controller.thank_you_letter(selection.name))
                    continue

        elif controller.user_input == '2':
            controller.create_report()
            continue

        elif controller.user_input == '3':
            controller.write_letter_to_file()
            continue
