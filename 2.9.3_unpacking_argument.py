# THIS CODE IS USED TO CALCULATE THE HEALTH


def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100 - age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)

bucky_data = [27, 20, 0]  # CREATED A LIST DATA


# THIS ARE THE TWO TYPES TO EXECUTE DATA LIST
health_calculator(bucky_data[0], bucky_data[1], bucky_data[2])
health_calculator(*bucky_data)

Suranjan_data = [18, 8, 1]

health_calculator(*Suranjan_data)

"""
	THIS CODE IS WORKING 
	1) WE CRETETED A LIST BECAUSE THERE ARE CHANCES THAT THERE WILL MANY PEOPLE WHO WNAT TO CALCULATE THERE HEALTH DATA
	2)* USING THIS WE CAN EXECUTE ALL THE DATA 
"""
