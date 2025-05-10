tasks = input('Enter your tasks for today separated by a comma: ').split(', ')

done_list = []

ongoing_list = []

for task in tasks:

    print(f'\n{task}\n')

    done = input(f'Did you finish {task} (yes or no): ').capitalize()

    if done == 'Yes':
        
        print('Nice job')

        done_list.append(task)

    elif done == 'No':

        print('Try to do it later')

        ongoing_list.append(task)

    else:

        print('Invalid choice')

    print('-------------------')

# Today's Progress

today_progress = input('Do you want to see your progress today: ').lower()

if today_progress == 'yes':

    print('     ***** DONE TASKS *****      ')

    print(done_list)

    print('    ***** ONGOING TASKS *****      ')

    print(ongoing_list)

else:

    input('Press enter to exit...')