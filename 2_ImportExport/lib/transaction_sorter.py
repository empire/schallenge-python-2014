import pickle
from lib.analysis_transactions import _get_reader
from sortedcontainers.sortedlist import SortedList
from transaction_commands.withdraw_command import WithdrawCommand

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def sorted_file_file_name_generator(sorted_files_names):
    index = 1
    while True:
        sorted_file_name = '/tmp/%d.ser'%index
        sorted_files_names.append(sorted_file_name)
        yield sorted_file_name
        index += 1


def dump_commands_to_file(command_list, file_name_generator):
    sorted_file_name = file_name_generator.next()
    with open(sorted_file_name, 'w') as fp:
        for cmd in reversed(command_list):
            pickle.dump(cmd, fp)


number_of_allowed_command = 40000

def sort_file_lists(input_file_list, file_name_generator):
    command_list = SortedList()
    for input_file in input_file_list:
        reader = _get_reader(input_file)
        for command in reader:
            command_list.add(command)
            if len(command_list) > number_of_allowed_command:
                dump_commands_to_file(command_list, file_name_generator)
                command_list = SortedList()


def merge_files(fp1, fp2, file_name_generator):
    out = open(file_name_generator.next(), 'w')
    rec1 = pickle.load(fp1)
    rec2 = pickle.load(fp2)
    while rec1 is not None or rec2 is not None:
        if rec2 is None or (rec1 is not None and rec1 >= rec2):
            pickle.dump(rec1, out)
            try:
                rec1 = pickle.load(fp1)
            except:
                rec1 = None
        else:
            pickle.dump(rec2, out)
            try:
                rec2 = pickle.load(fp2)
            except:
                rec2 = None


def merge_file_list(file_name_generator, sorted_files):
    while len(sorted_files) > 1:
        first_file = open(sorted_files.pop(0))
        second_file = open(sorted_files.pop(0))

        merge_files(first_file, second_file, file_name_generator)


def split_files(sorted_files):
    with open(sorted_files[0]) as fp:
        while True:
            try:
                rec = pickle.load(fp)
            except:
                break


def sort_transactions(input_file_list, base_name):
    sorted_files = []
    file_name_generator = sorted_file_file_name_generator(sorted_files)

    sort_file_lists(input_file_list, file_name_generator)
    merge_file_list(file_name_generator, sorted_files)
    split_files(sorted_files)
