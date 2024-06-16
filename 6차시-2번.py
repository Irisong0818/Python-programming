def get_student(student_list, key_value_list):
    candidate=[]
    for student in student_list:
        match=True
        for info in key_value_list:
            if student[info[0]]!=info[1]:
                match=False
                break
        if match:
            candidate.append(student)
    return candidate
    
student_database=[
    {'이름': '한넙죽', '학교': '한국중학교', '학년': 1, '연락처': '01012342345', '수업': ['Python', 'C']},
    {'이름': '김거위,', '학교': '오리초등학교', '학년': 5, '연락처': '01023334444', '수업': ['Python']},
    {'이름': '로라', '학교': '한국중학교', '학년': 2, '연락처': '01022354242', '수업': ['C++', 'Java']},
    {'이름': '리사', '학교': '한국초등학교', '학년': 6, '연락처': '01022223333', '수업': ['C', 'C++']},
    {'이름': '이철수', '학교': '대한초등학교', '학년': 5, '연락처': '01022448888', '수업': ['C', 'Python']},
    {'이름': '남영희', '학교': '대한중학교', '학년': 1, '연락처': '01023223333', '수업': ['Python', 'Java']}
]

print(get_student(student_database, [('학교','한국중학교')]))
print()
print(get_student(student_database, [('이름', '김로라'), ('학교','한국중학교')]))
print()
print(get_student(student_database, [('이름', '로라'), ('학교','한국중학교')]))