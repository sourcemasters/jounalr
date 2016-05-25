# Dirty Dozen Challenge, submission #2
# BASIC PROTOTYPE of a journaling app
#
# TODO: make saved entries permanent
# TODO: add timestamps and customizable titles
VERSION = "PROTOTYPE-1"
entries = list();
next_entry = 0

# main menu, options
def printMenu():
	print "Welcome to Journalr " + VERSION + "."
	print "What would you like to do?"
	print "1 Add an entry"
	print "2 Manage Entries"
	print "0 Exit"

def listEntries():
	for i in range(len(entries)):
		print "Entry " + str(i)

def manageEntries():
	global entries
	listEntries()
	print "\n3 Delete an Entry"
	print "4 Display an Entry"
	print "5 Delete all Entries"

	choice = raw_input(">")
	if (choice == "3"): # TODO: set guardian against invalid inputs
		to_delete = int(raw_input("Entry number to delete: "))
		del entries[to_delete]
		next_entry += -1
	elif (choice == "4"):
		to_display = int(raw_input("Entry number to display: "))
		print "Entry " + str(to_display)
		print entries[to_display]
	elif (choice == "5"):
		if (raw_input("Are you sure? y/n") == "y"):
			del entries
			next_entry = 0;


def start_program():
	global next_entry
	printMenu()
	option = raw_input("> ")
	while (option != "0"):
		printMenu()
		if (option == "1"):
			entries.append(raw_input("Journal Entry No " + str(next_entry) +":\n"))
			next_entry += 1
		elif (option == "2"):
			manageEntries()
		option = raw_input(">")

if __name__ == "__main__":
	start_program()