course_dict = {
    'AIコース': {'Aさん', 'Cさん', 'Dさん'},
    'Railsコース': {'Bさん', 'Cさん', 'Eさん'},
    'Railsチュートリアルコース': {'Gさん', 'Fさん', 'Eさん'},
    'JS': {'Aさん', 'Gさん', 'Hさん'},
}



def find_person(want_to_find_person):
    for course in course_dict.keys():
        if len(course_dict[course] & want_to_find_person) == 1 :
            print("{0}に{1}のみ在籍しています。".format(course, sorted(want_to_find_person & course_dict[course])))

        elif len(course_dict[course] & want_to_find_person)== 0:
            print("{0}に{1}は在籍していません。".format(course, sorted(want_to_find_person)))
        else:
            print("{0}に{1}が在籍しています。".format(course, sorted(want_to_find_person)))



def main():
    want_to_find_person = {'Cさん', 'Aさん'}
    print('探したい人: {}'.format(want_to_find_person))
    find_person(want_to_find_person)


if __name__ == '__main__':
    main()
