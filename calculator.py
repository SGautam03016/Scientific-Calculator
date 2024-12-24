#Create Calculator
import numpy as np
while True:
    print("\n---Calculator---")
    print("1.Addition")
    print("2.Subtractor")
    print("3.Multiplication")
    print("4.Division")
    print("5.Square Root")
    print("6.Logarithm")
    print("7.Statastic")
    print("8.Factorial")
    print("9.Exit")

    Chooice = int(input("Enter your choice between 1 to 7 :- "))
    if Chooice == 1:
        a1 = int(input("Enter First number you want find sum :- "))
        a2 = int(input("Enter Second number you want find sum :- "))
        addition = a1 + a2
        print("The Addition is :- ",addition)

    elif Chooice == 2:
        s1 = int(input("Enter First number you want find subtraction :- "))
        s2 = int(input("Enter Second number you want find Subtraction :- "))
        Subtraction = s1 - s2
        print("The Addition is :- ",Subtraction)

    elif Chooice == 3:
        m1 = int(input("Enter First number you want find Multiplication :- "))
        m2 = int(input("Enter Second number you want find Multiplication :- "))
        Multiplication = m1 * m2
        print("The Addition is :- ",Multiplication)

    elif Chooice == 4:
        d1 = int(input("Enter First number you want find Division:- "))
        d2 = int(input("Enter Second number you want find Division :- "))
        Division = d1 / d2
        print("The Addition is :- ",Division)

    elif Chooice == 5:
        square_root = float(input("Enter the number you want to find squaree root :- "))
        sr = np.sqrt(square_root)
        print("Square Root  :- ",sr)

    elif Chooice == 6:
        ch1 = input("Enter Chhoice (log,exp) :- ")
        if ch1 == 'log' :
            ch2 = input("Chhoice the nL(Natural log),lb(log base 10),lb2(log base 2)  :- ")
            if ch2 == 'nL':
                log = float(input("Enter the value you want to convert in log :- "))
                natural_log = np.log(log)
                print("The natural log :- ",natural_log)

            elif ch2 == 'lb':
                log_b = float(input("Enter the value you want to convert in log :- "))
                base_log = np.log10(log_b)
                print("The log base 10 is :- ",base_log)

            elif ch2 == 'lb2' :
                log_2 = float(input("Enter the value you want to convert in log :- "))
                log_base = np.log2(log_2)
                print("The log base 2  :- ",log_2)

        elif ch1 == 'exp'   :
            exp_1 = float(input("Enter the number you want to find Exponational :- "))
            exponational = np.exp(exp_1)
            print("The Exponational number :- ",exponational)  

    elif Chooice == 7 :
        ch3 = input("Chooise any option : \na = Mean \nb = Median \nc = Standard Daviation\nd = varriance \ne = Mod:-")
        if ch3 == 'a':
            
            num = int(input("Total numbers :- "))
            values = []
            for i in range(1,num+1):
                i = [int(input("Enter the value :-"))]
                values.append(i)
            mean = np.mean(values)
            print("Mean :- ",mean)

        elif ch3 == 'b':
            num = int(input("Total numbers :- "))
            values = []
            for i in range(1,num+1):
                i = [int(input("Enter the value :-"))]
                values.append(i)
            Median = np.median(values)
            print("Median :- ",Median)


        elif ch3 == 'c':
            num = int(input("Total numbers :- "))
            values = []
            for i in range(1,num+1):
                i = [int(input("Enter the value :-"))]
                values.append(i)
            Standard_d = np.std(values)
            print("Standard Deviation :- ",Standard_d)
            
        elif ch3 == 'e':
            num = int(input("Total numbers :- "))
            values = []
            for i in range(1,num+1):
                i = [int(input("Enter the value :-"))]
                values.append(i)
            mod = np.mod(values)
            print("Mod:- ",mod)

    elif Chooice == 8:
        n = int(input("Enter the number you want to the find factorial :- "))
        fact = 1
        for i in range(1,n+1):
            fact *= i
        print("The factorial is :- ",fact)

    elif Chooice == 11:
        print("Press 11 for one dimension :- ")
        print("Press 22 for Two dimension :- ")
        print("Press 33 for three dimension :- ")
        ch2 = int(input("Chocie any one number (11,22,33) :- "))
        if ch2 == 11 :
            print("Select A for matrix Addition :- ")
            print("Select B for matrix Subtraction :- ")
            print("Select C for matrix Multiplication :- ")
            ch3 = int(input("Choice Any character (A,B,C) :-"))
            if ch3 == 'A':
                print("1D Matrix Addition :- ")

            elif ch3 == 'B':
                print("1D Matrix Subtraction :- ")

            elif ch3 == 'C':
                print("1D Matrix Multiplication :- ")


        elif ch2 == 22 :   
            print("Select A for matrix Addition :- ")
            print("Select B for matrix Subtraction :- ")
            print("Select C for matrix Multiplication :- ")
            ch3 = int(input("Choice Any character (A,B,C) :-"))
            if ch3 == 'A':
                print("1D Matrix Addition :- ")

            elif ch3 == 'B':
                print("1D Matrix Subtraction :- ")

            elif ch3 == 'C':
                print("1D Matrix Multiplication :- ") 

        elif ch2 == 33 :   
            print("Select A for matrix Addition :- ")
            print("Select B for matrix Subtraction :- ")
            print("Select C for matrix Multiplication :- ")
            ch3 = int(input("Choice Any character (A,B,C) :-"))
            if ch3 == 'A':
                print("1D Matrix Addition :- ")

            elif ch3 == 'B':
                print("1D Matrix Subtraction :- ")

            elif ch3 == 'C':
                print("1D Matrix Multiplication :- ")           






