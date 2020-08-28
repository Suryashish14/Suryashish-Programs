school_name='BDM International'
exam_name='Periodic Test'
student_name='Suryashish Guha'
DOB='14/02/2005'
father='Surojit Guha'
mother='Ashissikta Guha'
subject1='English'
subject2='PE'
subject3='Mathematics'
subject4='Physics'
subject5='Chemistry'
subject6='Computer Science'
remarks='Well Done Keep It Up.'
marks1=72
marks2=76
marks3=75
marks4=74
marks5=75
marks6=77

total_marks=marks1+marks2+marks3+marks4+marks5+marks6
print('\n: : : : : : : : : : : : : : : REPORT CARD : : : : : : : : : : : :')
print('\n')
print('{:<15}'.format('School Name   - ')  ,school_name)
print('{:<15}'.format('Exam Name     - ')  ,exam_name)
print('{:<15}'.format('Student Name  - ') ,student_name)
print('{:<15}'.format('Date Of Birth - ') ,DOB)
print("Father's Name - ",father,"    Mother's Name - ",mother)
print('\n')
print('\n: : : : : : : : : : : : : : : MARKS : : : : : : : : : : : : : : :')
print('\n')
print('\n{:<16}'.format('Subject Name'),'   Marks')
print('\n{:<16}'.format(subject1),' = ',marks1)
print('\n{:<16}'.format(subject2),' = ',marks2)
print('\n{:<16}'.format(subject3),' = ',marks3)
print('\n{:<16}'.format(subject4),' = ',marks4)
print('\n{:<16}'.format(subject5),' = ',marks5)
print('\n{:<16}'.format(subject6),' = ',marks6)
print('\nTotal Marks - ',total_marks)
print('\nRemarks - ',remarks)