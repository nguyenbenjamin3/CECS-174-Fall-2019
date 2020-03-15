
annual_rate = float(input("Enter annual rate without % sign:"))
monthly_rate = annual_rate/1200
print('Your monthly rate is ', monthly_rate)
save_years = float(input("input years you plan on saving for:"))
save_months = (save_years*12)
print(save_years, "converted to months=", save_months)
monthly_inv = float(input("input monthly investment:"))
FV = (monthly_inv*(((1+monthly_rate)**save_months)-1)/monthly_rate)
print('The future value of your investment will be:', format(FV, '.2f'))

