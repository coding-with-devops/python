def main():   
    try:
        a = int(input("Enter You Input:"))
        print(a)
        return

    except Exception as e:
        print("Error Found")
        return

    finally:
        print("Script execution completed and Check Logs")
main()