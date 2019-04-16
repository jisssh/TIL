from mton.models import Student, Lecture, Enrolment

create_student = Student.objects.create
s1 = create_student(name='지상현')
s2 = create_student(name='지상큼')
s3 = create_student(name='지쓰짱')


l1 = Lecture.objects.create(title='알고리즘')
l2 = Lecture.objects.create(title='자료구조')
l3 = Lecture.objects.create(title='컴계')

Enrolment.objects.create(lecture=l1, student=s1)
Enrolment.objects.create(lecture=l1, student=s2)
Enrolment.objects.create(lecture=l1, student=s3)

지상현 = Student.objects.get(id=1)
지상현.enrolment_set.all()