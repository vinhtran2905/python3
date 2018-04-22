while True:
    try:
        number = int(input('what is your fav number?\n'))
        print('you got the range ' + str(18/number))
        break
    except ValueError:
        print('make sure and enter a number')
    except ZeroDivisionError:
        print('dont pick 0')
        #general if you dont know the specific error
    except:
        break
        # no matter option, execute a specfic code using finally
    finally:
        print('loop completed modified for featureabc')




