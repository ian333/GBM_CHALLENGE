def numberOfDays(y, m):
      bisiesto = 0
      if y% 400 == 0:
         bisiesto = 1
      elif y % 100==0:
         bisiesto=0
      elif y% 4 == 0:
         bisiesto = 1
      if m==2:
         return 28 + bisiesto
      list = [1,3,5,7,8,10,12]
      if m in list:
         return 31
      return 30