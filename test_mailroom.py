#!/usr/bin/env python

"""
Mailroom.py logic tests

"""

from mailroom import DonorData, ProgramController

# DonorData tests


def test_donor_data_name_is_correct():
    """
    tests if donor name is correctly added
    :return: None
    """
    # Arrange & Act
    test_donor1 = DonorData('Scott Guyton')

    # Assert
    assert test_donor1.name == 'Scott Guyton'


def test_donor_data_adds_multiple_donations():
    """
    tests if adding multiple donations works correctly
    :return: None
    """
    # Arrange
    test_donor2 = DonorData('James Brown')

    # Act
    test_donor2.add_donation(1, 2, 3)

    # Assert
    assert sum(test_donor2.donations) == 6
    assert len(test_donor2.donations) == 3

# ProgramController tests


def test_list_donors():
    """
    tests if list of donors returned is a reference to the controller's .donors property
    :return: None
    """
    # Arrange
    test_donor1 = DonorData('Scott Guyton')
    test_donor2 = DonorData('James Brown')
    test_donor3 = DonorData('Skream Benga')
    test_controller = ProgramController([test_donor1, test_donor2, test_donor3])

    # Act
    result = test_controller.list_or_add_donor('list')

    # Assert
    assert result is test_controller.donors


def test_select_donor_returns_correct_donor():
    """
    Tests if method .select_donor returns correct DonorData obj.
    :return: None
    """
    # Arrange
    test_donor1 = DonorData('Scott Guyton')
    test_donor2 = DonorData('James Brown')
    test_donor3 = DonorData('Skream Benga')
    test_controller = ProgramController([test_donor1, test_donor2, test_donor3])

    # Act
    result = test_controller.select_donor('Skream Benga')

    # Assert
    assert result is test_donor3


def test_select_donor_returns_none_and_adds_to_donor_list():
    """
    tests if donor is not found that it returns None & adds to donor list
    :return: None
    """
    # Arrange
    test_donor1 = DonorData('Scott Guyton')
    test_donor2 = DonorData('James Brown')
    test_donor3 = DonorData('Skream Benga')
    test_controller = ProgramController([test_donor1, test_donor2, test_donor3])

    # Act
    result = test_controller.list_or_add_donor('Kode9')

    # Assert
    assert result is None
    assert len(test_controller.donors) == 4
    assert test_controller.donors[-1].name == 'Kode9'


def test_thank_you_letter_returns_correct_name():
    # Arrange
    test_donor1 = DonorData('Scott Guyton')
    test_donor2 = DonorData('James Brown')
    test_donor3 = DonorData('Skream Benga')
    test_controller = ProgramController([test_donor1, test_donor2, test_donor3])

    # Act
    result = test_controller.thank_you_letter('Make me')

    # Assert
    assert result == 'Aloha Make me!\nWe here at the Mailroom LLC wish to give you mad props for sending a much needed' \
                 ' donation. We welcome your kindness, and again, a big mahalo to you from the MailRoom!'


def test_report_returns_correct_calculations():
    # Arrange
    test_donor1 = DonorData('Scott Guyton')
    test_donor2 = DonorData('James Brown')
    test_donor3 = DonorData('Skream Benga')
    test_controller = ProgramController([test_donor1, test_donor2, test_donor3])

    # Act
    for donor in test_controller.donors:
        donor.add_donation(1, 2, 3, 4, 5)

    # Assert
    for x in test_controller.donors:
        assert sum(x.donations) == 15
        assert len(x.donations) == 5
        assert sum(x.donations) / len(x.donations) == 3
