height = float(input('请出入你的身高（m）：'))
weight = float(input('请出入你的体重（kg）：'))

bmi = weight / (height * height)  #计算BMI指数

if bmi<18.5:
    print("BMI指数为：",str(bmi))
    print('体重过轻')
elif bmi>=18.5 and bmi<24.9:
    print("BMI指数为：",str(bmi))
    print('体重正常')
elif bmi>=24.9 and bmi<29.9:
    print("BMI指数为：",str(bmi))
    print('体重过重')
else:
    print("BMI指数为：",str(bmi))
    print('体重肥胖') 