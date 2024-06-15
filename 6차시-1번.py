#1번

def new_student(student_info):
    student_data={}
    #0. student_info 리스트 아래 5개 요소 길이 확인
    if len(student_info)!= 5:
        print("ERROR: studnet_info의 요소 수가 5가 아닙니다.")
        return {}
    #1. 학생 이름
    name=student_info[0]
    if type(name)==str:
        student_data['이름']=name
    else:
        print("ERROR: 이름이 str형이 아닙니다.")
        return {}
    #2. 학교명
    school=student_info[1]
    if type(school)==str:
        if "학교" in school:
            student_data['학교']=school
        else:
            print("ERROR: 학교 이름이 학교로 끝나지 않습니다.")
            return {}
    else:
        print("ERROR: 학교 이름이 str 타입이 아닙니다.")
        return {}
    #3. 학생 학년
    grade=student_info[2]
    if type(grade)==int and (0<=grade<7):
        student_data['학년']=grade
    else:
        print("ERROR: 학년이 7보다 작은 자연수가 아닙니다.")
        return {}
    #4. 학생 연락처
    contact=student_info[3]
    if type(contact)==str:
        if len(contact)==11:
            student_data['연락처']=contact
        else:
            print("ERROR: 연락처가 11자리가 아닙니다.")
            return {}
    #5. 학생 수업
    lesson=student_info[4]
    lessons=["Python", "Java", "C", "C++"]
    if type(lesson)==list:
        is_lesson=True
        for i in lesson:
            if i not in lessons:
                is_lesson=False
                break
        if is_lesson==False:
            print("ERROR: 수업은 lessons 리스트에 포함된 수업이어야 합니다.")
            return {}
        else:
            student_data["수업"]=lesson
    else:
        print("ERROR: 수업은 리스트 자료형으로 입력해야 합니다.")
        return {}
    print("새로운 학생의 정보를 완성했습니다: \n{}\n".format(student_data))

student_infos=[
    ['한넙죽', '한국중학교', 1, '01012342345', ['Python', 'C']],
    ['김거위,', '오리초등학교', 5, '01023334444', ['Python']],
    ['로라', '한국중학교', 2, '01022354242', ['C++', 'Java']],
    ['리사', '한국초등학교', 6, '01022223333', ['C', 'C++']],
    ['이철수', '대한초등학교', 5, '01022448888', ['C', 'Python']],
    ['남영희', '대한중학교', 1, '01023223333', ['Python', 'Java']]
]

student_infos_error=[
    ['한넙죽', '한국중학교', -1, '01012342345', ['Python', 'C']],
    ['김거위,', '오리초', 5, '01023334444', ['Python']],
    ['로라', '한국중학교', 2, '1022354242', ['C++', 'Java']],
    ['리사', '한국초등학교', 6, '01022223333', ['C', 'C++', 'English']],
    ['이철수', '대한초등학교', '5', '01022448888', ['C', "Python"]],
    ['남영희', 1, '대한중학교', '01023223333', ['Python', 'Java']]
]

for student_info in student_infos:
    new_st=new_student(student_info)

print("======== cut =========")
print()

for student_info_error in student_infos_error:
    new_student(student_info_error)
    