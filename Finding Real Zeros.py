#Jacob Hayes
#Finding All Real Zeros
#LC = Leading Coefficient; X2_1 = Original X^2; X_1 = Original X; Constant_2 = Second Constant; PZ = Possible Zero;
#X2_2 = Second X^2; X_2 = Second X; Constant_2 = Second Constant; Zero = should be a 0 after all the math is done.

import math

print "\n\t\t\t     *Finding Real Zeros*"

LRG_XPT = raw_input("\nIf there are only three Exponents, type \"Yes.\" If not type \"No.\" ")
 
if LRG_XPT == "Yes" or LRG_XPT == "yes" or LRG_XPT == "Y" or LRG_XPT == "y":
    LC_1 = float(raw_input("\nEnter the Leading Coefficient: "))

    X2_1 = float(raw_input("Enter the X^2 Coefficient: "))

    X_1 = float(raw_input("Enter the X Coefficient: "))

    Constant_1 = float(raw_input("Enter the Constant: "))

    def factor(n, noduplicates = False):
        intn = float(n)
        factors = {}
        lastfactor = n
        i = 0

        # 1 is a special case
        if n == 1:
            return {1: 1}

        while 1:
            i += 1

            # avoid duplicates like {1: 3, 3: 1}
            if noduplicates and lastfactor <= i:
                break

            # stop when i is bigger than n
            if i > n:
                break

            if n % i == 0:
                factors[i] = n / i
                lastfactor = n / i

        return factors

    print "\nFactors are +/-: " + str(factor(float(Constant_1), True))
    print "\nIf none of those work, try Putting each Above Factor / These Factors: " + str(factor(float(LC_1), True))

    PZ = float(raw_input("\nEnter A Factor: "))
    X2_2 = LC_1
    X_2 = (X2_1 + (X2_2 * PZ))
    Constant_2 = (X_1 + (X_2 * PZ))
    Zero = (Constant_1 + (Constant_2 * PZ))
    if Zero == 0:
        print "\n"
        print X2_2, ": New X^2."
        print X_2, ": New X."
        print Constant_2, ": New Constant."
        print Zero, ": Left-Over.\n"
    
        if PZ > 0:
            print PZ, "|", X2_2, "", X2_1, "  ", X_1, "  ", Constant_1
            print "    |      ", X2_2 * PZ , "   ", X_2 * PZ, " ", Constant_2 * PZ
            print "    |__________________________________"
            print      "     ", X2_2, "", X_2, "  ", Constant_2, "  ", Zero
    
        elif PZ < 0:
            print PZ, "|", X2_2, "  ", X2_1, "  ", X_1, "  ", Constant_1
            print "  |     ", X2_2 * PZ , "   ", X_2 * PZ, " ", Constant_2 * PZ
            print "   |__________________________________"
            print      "    ", X2_2, "  ", X_2, "  ", Constant_2, "  ", Zero

        raw_input("Press Enter to Continue...")
    
        print "\nf(x)=( X +", PZ * -1, ")(",X2_2, "\bx^2 +", X_2, "\bx +", Constant_2, ")."

        Multiply = Constant_2 * X2_2

        if Multiply < 0:
            Multiply = Multiply * -1
            print "\nFactors for M are +/-: " + str(factor(float(Multiply), True))
            print "\nEnter the factors that adds to be", X_2, "and go into", Multiply * -1, "\b."
            Add_1 = float(raw_input("Enter the First Factor: "))
            Add_2 = float(raw_input("Enter the Second Factor: "))

            Add_Total = Add_1 + Add_2
            Add_TotalM = Add_1 * Add_2
        
            if Add_Total == X_2 and Add_TotalM == Multiply * -1:
            
                print "\nf(x)=( X +", PZ * -1, ")(",X2_2, "\bx +", Add_1, ")(", X2_2, "\bx +", Add_2, ")."
                print "\n X=", PZ, "\b,", Add_1 * -1, "\b/", X2_2, "\b, and", Add_2 * -1, "\b/", X2_2, "\b."
                print "Reduce if Possible."
    
            else:
                print "\n\nPlease Retry with Different Numbers."
                print "\nFactors for M are +/-: " + str(factor(float(Multiply), True))
                print "\nEnter the factors that adds to be", X_2, "and goes into", Multiply * -1, "\b."
                Add_1 = float(raw_input("Enter the First Factor: "))
                Add_2 = float(raw_input("Enter the Second Factor: "))

                Add_Total = Add_1 + Add_2
                Add_TotalM = Add_1 * Add_2
        
                if Add_Total == X_2 and Add_TotalM == Multiply * -1:
            
                    print "\nf(x)=( X +", PZ * -1, ")(",X2_2, "\bx +", Add_1, ")(", X2_2, "\bx +", Add_2, ")."
                    print "\n X=", PZ, "\b,", Add_1 * -1, "\b/", X2_2, "\b, and", Add_2 * -1, "\b/", X2_2, "\b."
                    print "Reduce if Possible."

        elif Multiply > 0:
            print "\nFactors for M are +/-: " + str(factor(float(Multiply), True))
            print "\nEnter the factors that adds to be", X_2, "and goes into", Multiply, "\b."
            Add_1 = float(raw_input("Enter the First Factor: "))
            Add_2 = float(raw_input("Enter the Second Factor: "))
    
            Add_Total = Add_1 + Add_2
            Add_TotalM = Add_1 * Add_2
        
            if Add_Total == X_2 and Add_TotalM == Multiply:
            
                print "\nf(x)=( X +", PZ * -1, ")(",X2_2, "\bx +", Add_1, ")(", X2_2, "\bx +", Add_2, ")."

                if X2_2 == 1:
                    print "\n X=", PZ, "\b,", Add_1 * -1, "\b, and", Add_2 * -1, "\b."
                    print "\n\nThanks for Using My Software!"

                else:
                    print "\n X=", PZ, "\b,", Add_1 * -1, "\b/", X2_2, "\b, and", Add_2 * -1, "\b/", X2_2, "\b."
                    print "Reduce if Possible."

            else:
                print "\n\nPlease Retry with Different M factors."

                
        raw_input("\nPress Enter to Exit")

    else:   
        print "\nYou have", Zero, "left over."
        raw_input("Restart and try a new Factor")

elif LRG_XPT == "No" or LRG_XPT == "no" or LRG_XPT == "N" or LRG_XPT == "n":
    raw_input("\nThis program currently only works with three exponents. It may be updated to support four exponents.")

else:
    raw_input("\nYour command was unknown. Press enter and restart.")
