from abstraction import MarketCampaign

def main():
    campaign = MarketCampaign()

    while True:
        print("\nMarket Campaign")
        print("1) Create Campaign")
        print("2) Read Campaign")
        print("3) Update Campaign")
        print("4) Delete Campaign")
        print("5) Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            campaign.create_campaign()
        elif choice == "2":
            campaign.read_campaign()
        elif choice == "3":
            campaign.update_campaign()
        elif choice == "4":
            campaign.delete_campaign()
        elif choice == "5":
            print("Exiting Market Campaign system.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()