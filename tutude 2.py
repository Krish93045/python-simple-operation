def main():
    print("Personalized Greeting Program")
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    if not first_name or not last_name:
        print("Both first name and last name must be provided.")
        return

    full_name = f"{first_name} {last_name}"
    print(f"Hello, {full_name}! Welcome to the Python programming course.")

if __name__ == "__main__":
    main()
