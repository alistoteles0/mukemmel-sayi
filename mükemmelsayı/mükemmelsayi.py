print("Girilen bir sayının mükemmel sayı olup olmadığını söyleyen program.")

while True:
    try:
        a = int(input("Lütfen pozitif bir tam sayı giriniz: "))
        break
    except ValueError:
        print("Lütfen geçerli bir değer giriniz.")
bölen = 0
if a > 0:
    for i in range(1,a):
        if a % i == 0:
            bölen += i
            if bölen == a:
                print("Girdiğiniz sayı mükemmel sayıdır.")
    if bölen != a:
        print("Girdiğiniz sayı mükemmel sayı değildir.")
else:
    print("Lütfen geçerli bir değer giriniz.")

    
            
    
        