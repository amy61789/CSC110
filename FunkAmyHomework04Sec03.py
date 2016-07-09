# Project:      Homework 4 (FunkAmyHomework04Sec03.py)
# Name:         Amy Funk
# Date:         05/24/2016
# Description:  Program will determine cost ocoffee order input by user.
#               It will display a summary of coffee type, # of lbs, sub-total,
#               shipping and handling costs, city and state it's being
#               shipped to, delivery method, payment type, tax, and total.


# defines the shipping and handling function
def fltSandH(fltCoffeePounds):

    # returns the value of shipping and handling costs
    return (fltCoffeePounds * 0.93) + 2.50

# defines the delivery type function
def intDeliveryType(strDeliveryType):

    # applies the lower method to the delivery type string
    strDeliveryType = strDeliveryType.lower()

    # if delivery type is overnight method
    if strDeliveryType == "on":

        # return delivery type value of 20
        return 20

    # if delivery type is two-day
    elif strDeliveryType == "2d":

        # return delivery type value of 13
        return 13

    # if delivery type is standard
    elif strDeliveryType == "std":

        # return delivery type value of 0
        return 0
    
    # if none of the previous conditions are equal to the input
    else:

        # prints an error message telling user to enter a valid delivery type
        print("ERROR: Please enter a valid Shipping and Handling type.")

# defines the tax function
def fltTax(strStateTax):

    # applies the upper method to the state tax string
    strStateTax = strStateTax.upper()

    # if the length of input from user is equal to two characters
    if len(strStateTax) == 2:

        # checks if input matches WA CA or TX
        if strStateTax == "WA" or strStateTax == "CA" or strStateTax == "TX":

            # returns tax value of 9%
            return 0.09

        # checks if input matches OR or FL
        elif strStateTax == "OR" or strStateTax == "FL":

            # returns tax value of 0%
            return 0
        
        # all other states 
        else:

            # return tax value of 7%
            return 0.07
    # input length is not equal to 2
    else:

        # prints error message to enter a valid state code
        print("ERROR: Please enter a valid state code.")

# defines the Subtotal function
def fltSubtotal(strCoffeeType,fltCoffeePounds):

    # if coffee type is equal to Jonestown Brew
    if strCoffeeType == "JONESTOWN BREW":

        # returns coffee price is equal to pounds multiplied by 10.50 (Jonestown Brew price per lb)
        return fltCoffeePounds * 10.50

    # if coffee type is equal to Plymouth Jolt
    elif strCoffeeType == "PLYMOUTH JOLT":

        # returns coffee price is equal to pounds multiplied by 16.95 (Plymouth Jolt price per lb)
        return fltCoffeePounds * 16.95

    # if input does not equal Jonestown Brew or Plymouth Jolt
    else:

        # prints error message to input valid coffee type
        print("ERROR: Please enter a valid coffee type.")
        
# defines the payment options function
def fltPaymentOptions(strPaymentChoice):

    # applies the upper method to the payment choice string
    strPaymentChoice = strPaymentChoice.upper()

    # if condition is equal to paypal
    if strPaymentChoice == "PP":

        # returns a 3% payment fee
        return 0.03

    # if condition is equal to credit card
    elif strPaymentChoice == "CC":

        # returns a 5% payment fee
        return 0.05

    # if condition is equal to check
    elif strPaymentChoice == "CK":

        # returns a 2% discount
        return -0.02

    # if no previous condtions were equal to a payment choice
    else:

        # prints error message to enter a valid payment option
        print("ERROR: Please enter a valid Payment Option.")
        
# defines the main coffee function
def mainCoffee():

    # prints user greeting when program is run, what to input for each selection and prices/fees
    print("##### KONDITOREI COFFEE SHOP #####\n",
          "THE COFFEE TYPES AVAILABLE ARE: \n\n*JONESTOWN BREW* ### $10.50/LB ###\n*PLYMOUTH JOLT* ### $16.95/LB ###\n"
          "TYPE 'JONESTOWN BREW' OR 'PLYMOUTH JOLT' TO INDICATE WHICH COFFEE YOU WOULD LIKE\n\n",
          "SHIPPING METHODS AVAILABLE ARE: \n\n*OVERNIGHT* = ON ### $20.00 ###\n*TWO DAY* = 2D ### $13.00 ###\n*STANDARD* = STD ### $0.00 ###\n\n",
          "PAYMENT OPTIONS AVAILABLE ARE: \n\n*PAYPAL* PLUS 3% FEE = PP\n*CREDIT CARD* PLUS 5% FEE = CC\n*CHECKS* 2% DISCOUNT = CK\n\n",)
          
    # prompts the user to input what type of coffee they would like to purchase
    strCoffeeType = str(input("Please enter the type of coffee you would like to purchase: "))

    ## TRY EXCEPT BLOCK ##
    try:

        ## prompts user to input how many pounds of coffee ##
        ## they would like to purchase ##
        fltCoffeePounds = float(input("How many pounds would you like to purchase: "))

    ## catches the program from blowing up due to invalid ##
    ## user input ##
    except:
        
        # prints error message to input a numerical value
        print("ERROR: Please enter in a numerical value.")

    # prompts user to input a city for delivery
    strCity = str(input("Please enter city for delivery: "))

    # prompts user to input state for delivery
    strStateTax = str(input("Please enter state for taxes and delivery: "))

    # prompts user to input a shipping method 
    strDeliveryType = str(input("Please enter a valid shipping method you would like to use: "))

    # prompts user to input a payment option
    strPaymentChoice = str(input("Please enter the payment option you would like to use: "))

    # applies the upper method to the coffee type entered by user
    strCoffeeType = strCoffeeType.upper()

    # calls the fltSubtotal function to return the coffee price
    fltCoffeePrice = fltSubtotal(strCoffeeType,fltCoffeePounds)
    
    # tax fees is equal to state tax multiplied by the coffee price
    fltTaxFees = fltTax(strStateTax) * fltCoffeePrice

    # calls intDelveryType function to return value of delivery
    intDelivery = int(intDeliveryType(strDeliveryType))

    # calls the fltPaymentOptions function to return value of payment option
    # multiplied by the coffee price to equal fltPaymentTypeFee
    fltPaymentTypeFee = fltPaymentOptions(strPaymentChoice) * fltCoffeePrice

    # calculates the total price of the order
    fltTotal = fltCoffeePrice + fltSandH(fltCoffeePounds) + intDelivery + fltPaymentTypeFee + fltTaxFees

    # prints coffee order summary
    print("##### ORDER SUMMARY #####\n\n",
          #prints coffee type
          "*COFFEE TYPE*:", strCoffeeType,"\n\n",
          # prints how many pounds ordered
          "*POUNDS ORDERED*:", fltCoffeePounds,"\n\n",
          # prints subtotal of coffee order formatted for US currency
          "*SUBTOTAL*: ${0:0.2f}".format(fltCoffeePrice),"\n\n",
          # prints S&H fees and invokes the fltSandH function formatted for US currency
          "*SHIPPING AND HANDLING FEES*: ${0:0.2f}".format(fltSandH(fltCoffeePounds)),"\n\n",
          # prints city entered in all uppercase
          "*CITY*:", strCity.upper(),"\n\n",
          # prints state entered in all uppercase
          "*STATE*:", strStateTax.upper(),"\n\n",
          # prints delivery method and invokes intDeliveryType function formatted for US currency
          "*DELIVERY METHOD*:", strDeliveryType.upper(),"${0:0.2f}".format(intDeliveryType(strDeliveryType)),"\n\n",
          # prints payment type and invokes fltPaymentOptions function formatted for US currency
          "*PAYMENT TYPE*:", strPaymentChoice.upper(),"${0:0.2f}".format(fltPaymentTypeFee),"\n\n",
          # prints tax fees formatted for US currency
          "*TAX FEES*: ${0:0.2f}".format(fltTaxFees), "\n\n",
          # prints total cost of order formatted in US currency
          "*TOTAL*: ${0:0.2f}".format(fltTotal))
    
# calls/invokes the mainCoffee function
mainCoffee()    
        
    
