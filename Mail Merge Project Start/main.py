#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

invited_names = open('C:/Users/Hemanth kumar s/Documents/mail merge/Mail Merge Project Start/Input/Names/invited_names.txt')
names = invited_names.readlines()
new_names = []
invited_names.close()
for i in names:
    x = i.replace("\n", "")
    new_names.append(x)

mail = open('C:/Users/Hemanth kumar s/Documents/mail merge/Mail Merge Project Start/Input/Letters/starting_letter.txt')
mail_content = mail.readlines()
mail.close()

for i in new_names:
    x = mail_content[0]
    y = x.replace("[name]", i)
    mail_content[0] = y
    z = open(f'letter_for_{i}.txt', 'w')
    for j in mail_content:
        z.write(j)
    mail_content[0] = x

z.close()

