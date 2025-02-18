class Marketoperations:
    def __init__(self):
        self.campaigns = []

    def create_campaign(self):
        campaign_name = input("Enter campaign name: ")
        campaign_details = input("Enter campaign details: ")
        campaign = {"name": campaign_name, "details": campaign_details}
        self.campaigns.append(campaign)
        print(f"Campaign '{campaign_name}' created successfully!")

    def read_campaign(self):
        print(self.campaigns)

       # for campaign in self.campaigns:
         #   if campaign["name"] == campaign_name:
             #   campaign["details"] += f"; {additional_details}"
              #  print(f"Details added to campaign '{campaign_name}'!")
             #   return
        # print(f"Campaign '{campaign_name}' not found!")

    def update_campaign(self):
        campaign_name = input("Enter the name of the campaign to update: ")

        for campaign in self.campaigns:
            if campaign["name"] == campaign_name:
                new_name = input("Enter the new name for the campaign: ")
                new_details = input("Enter the new details for the campaign: ")
                campaign["name"] = new_name
                campaign["details"] = new_details
                print(f"Campaign '{campaign_name}' updated successfully!")
                return
        print(f"Campaign '{campaign_name}' not found!")

    def delete_campaign(self):
        campaign_name = input("Enter the name of the campaign to delete: ")

        for campaign in self.campaigns:
            if campaign["name"] == campaign_name:
                self.campaigns.remove(campaign)
                print(f"Campaign '{campaign_name}' deleted successfully!")
                return
        print(f"Campaign '{campaign_name}' not found!")
