question_list = [
"How many continents are there?",
"What is the capital of India?",
"NG mei kaun se course padhaya jaata hai?",
"Navgurukul ka daiy schedule kab se kab tak h",
"The language of lakshadweep,a union territory of india ,is",
"If you call someone ‘Makkhichoos’, then what are you calling him?",
"What is the term use for shops that provide the buyer exemption from certain taxes ?",
"pyar or dosti me kya hai?",
"Aap duniya me mamma papa ke alawa sabse jyada time or pyar kisi dena pasand karoge?"
]
options_list = [
["Four", "Nine", "Seven", "Eight"],
["Chandigarh", "Bhopal", "Chennai", "Delhi"],
["Software Engineering", "Counseling", "Tourism", "Agriculture"],
["8 to 9 O'clock", "9 to 9 O'clock","10 to 9 O'clock", "11 to 9 O'oclock"],
["Malyalam","Hindi", "English","tamil"],
["Evil","Humble" ,"Dishonest","Miserly"],
["Care-Free","Duty-Free","Job-Free","Rate-Free"],
["Dono dil ke reshty hai", "Ek dil ka to dusra dimag ka","Dil or jasbat ka reshta hai"],
["Dost","Lover","Dil ke karib hai uske sath","Kud ke sath"]
]
op50_50=[["1)Four","3)Seven"],
["2)Bhopal","4)New delhi"],
["1)Software engineering","2)Counseling"],
["2) 9 to 9 O'clock","1) 8 to 9 O'clock"],
["3) English","1)Malyalam"],
["4) Miserly","1)Evil"],
["2) Duty-free","4)Rate-free"],
["1) Dono dil ke reshty hai","3)Dil or jasbat ka reshta hai"],
["1)Dost","3)Dil ke karib hai uske sath"]]

answer_list=[3,4,1,2,1,4,2,1,3] 
print("WELCOME TO  KBC 🙏")
print("Kon Banega Karodpati 💰 Aao or Khelo Game or Jito Price🏆 🥇")
print("Lest Start Game 👍")
i=0
c=0
s=10000
while i<len(question_list):
    print(question_list[i])
    a=0
    while a<len(options_list[i]):
        k=options_list[i][a]
        print(a+1,k)
        a+=1
    if c==0:
        life_line=input("Do you want to use life line 🤔 ?:-")
        if life_line=="yes":
            c+=1
            print(op50_50[i])
            s+=100000
    Ans=int(input("Enter your option:-"))
    if answer_list[i]==Ans:
        print("Your answer is correct,you won 🤗",s,"Rupees 😊")
        s+=100000
    else:
        print("Your answer is wrong 😕 🙁")
        break
    i+=1                






