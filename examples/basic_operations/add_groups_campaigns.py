from google.ads.googleads.client import GoogleAdsClient
import argparse
import os
from pathlib import Path
try:
    from examples.basic_operations import add_campaigns
    from examples.basic_operations import add_ad_groups
except:
    import add_campaigns
    import add_ad_groups

direct = Path(__file__).parents[2]
print(direct)
path_txt = os.path.join(direct, 'brands.txt')

with open(path_txt, 'r') as f:
    lines = f.readlines()
    brand_list = [line.strip() for line in lines]
print(brand_list)
def main(customer_id):
    """Function that create campaigns and ad group for certain customer id"""
    # GoogleAdsClient will read the google-ads.yaml configuration file in the
    # home directory if none is specified.
    global brand_list
    client = GoogleAdsClient.load_from_storage(version="v12")
    for brand in brand_list:
        for num in range(1,3):
            campaigns_id = add_campaigns.main(client,customer_id,brand,num)
            add_ad_groups.main(client,customer_id,campaigns_id,brand)


if __name__ == "__main__":
    # GoogleAdsClient will read the google-ads.yaml configuration file in the
    # home directory if none is specified.
    googleads_client = GoogleAdsClient.load_from_storage(version="v12")

    parser = argparse.ArgumentParser(
        description="Adds a campaign for specified customer."
    )
    # The following argument(s) should be provided to run the example.
    parser.add_argument(
        "-c",
        "--customer_id",
        type=str,
        required=True,
        help="The Google Ads customer ID.",
    )
    args = parser.parse_args()
    cust_id = args.customer_id

    for brand_name in brand_list:
        for i in range(1,3):
            camp_id = add_campaigns.main(googleads_client,cust_id,brand_name,i)
            add_ad_groups.main(googleads_client,cust_id,camp_id,brand_name)
