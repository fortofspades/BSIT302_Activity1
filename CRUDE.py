Pantsu = ["Dickies","Adidas","Nike"]
slct = True
while slct:
	print("""
*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
		1. Add a pair of pants
		2. Remove a pair of pants
		3. Update a pair of paints
		4. Look-up a pair of pants
		5. Stop
		""")

	slct = input ("What would you like to do? ")
	if slct =="1":
		create = str (input ("Name your pair of pants: "))
		Pantsu.append(create)
		print ("Added " + create + " to your pants")
		print (Pantsu)

	elif slct=="2":
		print (Pantsu)
		void = int (input ("Enter index number of pants to remove: "))
		print ("Would you like to delete? " + Pantsu[void])
		pop = True
		while pop:
			boolean = str (input(" Yes or No?"))
			if boolean == "Yes":
				print ("Successfully deleted " + Pantsu[void])
				
				print ("These are the pair of pants: " + Pantsu.pop(void))
				print (Pantsu)
				pop = None
				
			elif boolean == "No":
				print ("No pants were deleted: ")
				print (Pantsu)
				pop = None
			else:
				print ("Invalid Choice")

	elif slct == "3":
		print (Pantsu)
		update = int (input ("Enter index number(0-2+) of pants to update: "))
		print (Pantsu[update] + " is selected")
		updated = str (input ("What would you like to change it to? "))
		Pantsu[update] = updated
		print ("Change successful!")
		print (Pantsu)

	elif slct == "4":
		print ("Viewing pants: ")
		print (Pantsu)

	elif slct == "5":
		print ("--- S T O P P E D ---")
		slct = None

	else:
		print ("Invalid Selection")

			