phonebook={"Suhel":9876543210,"Ravi":9123456780,"Anita":9988776655}
search=input("Search Name:")
if search in phonebook:
    print(f"Phone Number of {search}:{phonebook[search]}")