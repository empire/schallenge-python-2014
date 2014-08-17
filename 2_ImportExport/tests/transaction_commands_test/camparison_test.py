from transaction_commands.deposit_command import DepositCommand
from transaction_commands.transfer_command import TransferCommand
from transaction_commands.withdraw_command import WithdrawCommand

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def test_compare_deposit_command():
    highest1 = DepositCommand(2, amount=17)
    lowest = DepositCommand(3, amount=11)
    highest2 = DepositCommand(5, amount=17)

    check(highest1, lowest, highest2)

def test_compare_withdraw_command():
    highest1 = WithdrawCommand(2, amount=17)
    lowest = WithdrawCommand(3, amount=11)
    highest2 = WithdrawCommand(5, amount=17)

    check(highest1, lowest, highest2)

def test_compare_transfer_command():
    highest1 = TransferCommand(2, 3, amount=17)
    lowest = TransferCommand(3, 5, amount=11)
    highest2 = TransferCommand(5, 7, amount=17)

    check(highest1, lowest, highest2)

def test_compare_together():
    deposit_command = DepositCommand(5, 7)
    transfer_command = TransferCommand(5, 2, 7)
    withdraw_command = WithdrawCommand(5, 7)

    check(withdraw_command, deposit_command)
    check(withdraw_command, transfer_command)
    check(deposit_command, transfer_command)


def check(highest1, lowest, highest2 = None):
    assert highest1 > lowest
    assert lowest < highest1

    assert highest1 >= lowest
    assert lowest <= highest1

    assert not(highest1 < lowest)
    assert not(lowest > highest1)

    assert not(highest1 <= lowest)
    assert not(lowest >= highest1)

    assert not(highest1 == lowest)
    assert not(lowest == highest1)

    assert highest1 != lowest
    assert lowest != highest1

    if None == highest2:
        return

    assert highest1 == highest2
    assert highest1 != lowest
    assert not(highest1 != highest2)
    assert not(highest1 != highest1)
