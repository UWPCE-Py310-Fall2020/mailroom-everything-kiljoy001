from mailroom.Mailroom_Classes import ProgramController, MenuController, DonorData

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
controller = ProgramController()
menu = MenuController()


def main():
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

