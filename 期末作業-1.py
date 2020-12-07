import random
import time

restart = True
while restart:
    answer = ''
    a_count=0
    b_count=0
    z_times=0

    print("輸入4位數字，數字和位置答對會顯示A，只有數字答對則會顯示B，若都沒有則會顯示0A0B，假設您輸入的數字為4321，答案為5124，則會顯示1A2B\n 引用 張泰睿 說:人生可以很輕鬆，只要call out 阿姨\"我想少奮鬥十年\"\n")
    print("本遊戲有計時，從畫面即開始計時!!\n")
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    answer=''
    random.shuffle(items)


    for i in range(4):
        answer+=str(items[i])
        start = time.time() #開始時間
            



    while(True):

        
        number=input("請輸入四個數字(且不能重複數字):")
       

        if(number=="我想少奮鬥十年"):
            z_times+=1
            print("答案:%s\n" % answer)

        elif(number == "我想要提示"):
            z_times+=1
            guess=input("你想要第幾位數的提示:")
            if(guess=="1"):
                if(items[0]==0):
                    print("第一位為0")
                elif(items[0]==1):
                    print("第一位為1")
                elif(items[0]==2):
                    print("第一位為2")
                elif(items[0]==3):
                    print("第一位為3")
                elif(items[0]==4):
                    print("第一位為4")
                elif(items[0]==5):
                    print("第一位為5")
                elif(items[0]==6):
                    print("第一位為6")
                elif(items[0]==7):
                    print("第一位為7")
                elif(items[0]==8):
                    print("第一位為8")
                else:
                    print("第一位為9")

            elif(guess=="2"):
                if(items[1]==0):
                    print("第二位為0")
                elif(items[1]==1):
                    print("第二位為1")
                elif(items[1]==2):
                    print("第二位為2")
                elif(items[1]==3):
                    print("第二位為3")
                elif(items[1]==4):
                    print("第二位為4")
                elif(items[1]==5):
                    print("第二位為5")
                elif(items[1]==6):
                    print("第二位為6")
                elif(items[1]==7):
                    print("第二位為7")
                elif(items[1]==8):
                    print("第二位為8")
                else:
                    print("第二位為9")


            elif(guess=="3"):
                if(items[2]==0):
                    print("第三位為0")
                elif(items[2]==1):
                    print("第三位為1")
                elif(items[2]==2):
                    print("第三位為2")
                elif(items[2]==3):
                    print("第三位為3")
                elif(items[2]==4):
                    print("第三位為4")
                elif(items[2]==5):
                    print("第三位為5")
                elif(items[2]==6):
                    print("第三位為6")
                elif(items[2]==7):
                    print("第三位為7")
                elif(items[2]==8):
                    print("第三位為8")
                else:
                    print("第三位為9")


            elif(guess=="4"):
                if(items[3]==0):
                    print("第四位為0")
                elif(items[3]==1):
                    print("第四位為1")
                elif(items[3]==2):
                    print("第四位為2")
                elif(items[3]==3):
                    print("第四位為3")
                elif(items[3]==4):
                    print("第四位為4")
                elif(items[3]==5):
                    print("第四位為5")  
                elif(items[3]==6):
                    print("第四位為6")
                elif(items[3]==7):
                    print("第四位為7")
                elif(items[3]==8):
                    print("第四位為8")
                else:
                    print("第四位為9")



            else:
                print("都給你機會還手殘\n")

        elif(len(number) !=4):
            z_times+=1
            print("叫你輸入四個看不懂嗎??\n")


        else:

            z=list(number)


            if(z[0] == z[1] or z[0] == z[2] or z[0] == z[3] or z[1] == z[2] or z[1] == z[3] or z[2] == z[3] ):#排除重複數字的狀況，利用將輸入資料轉乘list一一去檢查
                z_times+=1
                print("你去死\n")

            else:
                number="".join(z) #將list轉成字串

                if (not number.isdigit()):
                    z_times+=1
                    print("你輸入的不是數字，請輸入四個數字\n")
                else:
                    if(number==answer):
                        z_times+=1
                        end = time.time() #結束時間
                        print("恭喜你猜對數字!\n")
                        print("總共花了 %d次\n" % z_times)
                        print("執行時間 %f秒" %(end-start))
                        cont = input("是否繼續遊玩(y/n)")
                        if (cont == "n"):
                            restart = False
                            break
                        elif (cont == "y"):
                            answer=''
                            random.shuffle(items)

                            z_times=0
                            for i in range(4):
                                answer+=str(items[i])
                                start = time.time() #開始時間
                            continue
                    else:
                        for i in range(4):
                            for j in range(4):
                                if i==j and number[i]==answer[j]:
                                    a_count+=1
                                    z_times+=1
                                elif number[i]==answer[j]:
                                    b_count+=1
                                    z_times+=1

                        print('{0}A{1}B\n'.format(a_count,b_count))

                        a_count=0
                        b_count=0
