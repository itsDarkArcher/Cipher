# Secure-Pass
#Inside the folder you will find 2 python modules

one is the password generator
it creates a password choosing a list of personalized words and a number randomly

then it encrypts the new password and saves it in a .plk file
and returns the word and number that the program used to create the password
#That is important bc you will use those words and numbers to later decrypt the password to use

#The second file extracts the key from the .pkl file and uses to decryp the password but only when the user inserts the word and the number previously given by the first module 

#### For major security insert your own words on the list in the generator #####
### DO NOT DELETE THE KEYWORDS FILE ONCE ITS CREATED OR YOU WILL LOOSE THE DECRYPTION KEY####

The main porpuse is to create random passwords that you can only access thru the program 
And in that way you can safely storage the Words and Numbers that created them and no one but the user could decrypt it
