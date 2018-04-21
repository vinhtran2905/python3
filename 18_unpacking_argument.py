def health_calculator(age,apples_ate,cig_smoked):
    answer = (100-age) + (apples_ate * 3.5) - (cig_smoked * 2)
    print(answer)


vinh = [37,20,0]
health_calculator(vinh[0],vinh[1],vinh[2])
#unpacking argument
health_calculator(*vinh)