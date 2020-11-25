import os
import sys


# functions
####################################################################################################

# function to, given a list of strings and a keyword, print the strings (data lines) which contains the keyword
def print_relevant_data(data_lines_container, keyword):
    it = 0
    # iterate over the list of data (lines from the txt containing the ffmpeg analysis)
    for i in range(len(data_lines_container)):
        # if found print the data
        if data_lines_container[i].find(keyword) > -1:
            it = it + 1
            # print this only once
            if (it == 1):
                print('\nRelevant data from the container with the keyword', '"', keyword, '":')
            # print all the lines containing the keyword
            print('\n', data_lines_container[i], '\n')


####################################################################################################

cont = 'n'

while (cont == 'n'):
    option = input(
        '\nChoose an exercise:\n1. Three relevant data from the BBB.mp4 container.\n2. Rename file.\n3. Resize '
        'file.\n4. Transform the input file codec.\n5. Exit\n\nOption: ')
    if option == '1':
        # exercise 1:
        # translate ffmpeg analysis info into a txt file
        os.system('ffmpeg -i material/bbb_original.mp4 2> material/output_data.txt')

        # read info in txt file
        f = open('material/output_data.txt', 'r')

        # convert lines of the txt file to list of str
        lines = f.readlines()

        # considering video, audio and duration the 3 relevant data items from the bbb container video
        # it will show information about the audio and video streams
        print_relevant_data(lines, 'Video')
        print_relevant_data(lines, 'Audio')
        print_relevant_data(lines, 'Duration')

        f.close()

    elif option == '2':
        # exercise 2
        print('\nWARNING: Enter the new file name with the .mp4 extension (example: new_name.mp4).\n')
        continue_ = 'y'
        while continue_ == 'y':
            old_name = input('\nFile to rename: ')  # which file you want to rename (only name, not the path)
            new_name = input('Rename file ' + old_name + ' as: ')  # new name
            old_name = 'material/' + old_name  # path (inside material folder)
            new_name = 'material/' + new_name
            os.rename(old_name, new_name)  # rename
            continue_ = input('Rename another file?[y/n] ')  # in order to rename more files

    elif option == '3':
        # exercise 3
        input_file = input('Video/image to resize: ')  # video or image to resize
        width = input('New width: ')
        height = input('New height: ')
        order = 'ffmpeg -i material/' + input_file + ' -vf scale=' + width + ':' + height + ' material/new_' + width + \
                'x' + height + '.mp4'  # ffmpeg order
        os.system(order)

    elif option == '4':
        # exercise 4
        input_file = input('Video to convert: ')  # video name to convert (only name, not the path)
        input_file = 'material/' + input_file  # path (inside material folder)
        order = 'ffmpeg -i ' + input_file + ' material/new_video.mpeg'  # convert input mp4 to mpeg1
        os.system(order)

    elif option == '5':
        # exit: stop the program
        break

    cont = input('Close program?[y/n] ')
    option = ''
