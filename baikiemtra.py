from guizero import *
app=App(title='Bài kiểm tra', width=1000, height=800)
box1=Box(app,layout='grid')
text=Text(box1,text='Họ và Tên:',grid=[0,0])
text1=Text(box1,text='Lớp:',grid=[0,1])
hovaten=TextBox(box1,width=30,grid=[1,0])
lop=TextBox(box1,width=30,grid=[1,1])
box2=Box(app,layout='grid')
nopbai=PushButton(box1,text='Nộp Bài',grid=[2,0],command=)
def ():
    with open (f'cauhoi.txt', 'w', encoding='utf-8')as file:
        file.write('1 + 123 x 2 : 2 = ?')
def danhsachcauhoi():
    global nhapcauhoi
    cauhoi=nhapcauhoi.value
    with open (f'cauhoi.txt', 'r', encoding='utf-8')as file:
        cauhoi=file.read()
caccauhoi=ListBox(box2,height=100,width=300,grid=[0,0],items=[],command=danhsachcauhoi)
nhapcauhoi=TextBox(box2,text='',width=20,height=10,grid=[1,0],command=)
app.display()
