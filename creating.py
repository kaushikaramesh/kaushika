def check_Power(M,k):
    if M <= 0 or k <=0:
        print "not a valid input"
    else:
        for i in range (1,20):
            x = k**i
            if x == M :
                print " True "
                print k, "power ", i , "is", M
                break
            elif x> M:
                print "false"
                break
