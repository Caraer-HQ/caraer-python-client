# SimplePublicCompanyDTO

Data Transfer Object representing a public-facing view of a company

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier of the company | [optional] 
**updated_at** | **int** | Timestamp of the last update (in milliseconds since epoch) | [optional] 
**website** | **str** | The website URL of the company | [optional] 
**cookie_policy** | **str** | Cookie policy URL of the company | [optional] 
**favicon** | **str** | Path to the company&#39;s favicon | [optional] 
**privacy_policy** | **str** | Privacy policy URL of the company | [optional] 
**accent_color** | **str** | The accent color used by the company | [optional] 
**twitter_url** | **str** | Twitter URL of the company&#39;s social media page | [optional] 
**primary_color** | **str** | The company&#39;s primary color used in branding | [optional] 
**terms_and_conditions** | **str** | Terms and conditions URL of the company | [optional] 
**facebook_url** | **str** | URL to the company&#39;s Facebook page | [optional] 
**youtube_url** | **str** | URL to the company&#39;s YouTube page | [optional] 
**company_color** | **str** | Company&#39;s branding color | [optional] 
**name** | **str** | Name of the company | [optional] 
**logo** | **str** | Path to the company&#39;s logo image | [optional] 
**instagram_url** | **str** | URL to the company&#39;s Instagram page | [optional] 
**font_color** | **str** | Font color used in company&#39;s branding | [optional] 
**secondary_color** | **str** | Secondary color used in company&#39;s branding | [optional] 
**right_nav_bar_button_enabled** | **bool** | Boolean flag indicating if the right navigation bar button is enabled | [optional] 
**right_nav_bar_button_title** | **str** | Title of the right navigation bar button | [optional] 
**right_nav_bar_button_link** | **str** | Link for the right navigation bar button | [optional] 
**css_script** | **str** | CSS scripts added by the company | [optional] 
**js_head_script** | **str** | JavaScript code injected into the head tag of the HTML page | [optional] 
**js_body_script** | **str** | JavaScript code injected into the body tag of the HTML page | [optional] 
**custom_domain** | **str** | Custom domain name used by the company | [optional] 

## Example

```python
from caraer_client.models.simple_public_company_dto import SimplePublicCompanyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SimplePublicCompanyDTO from a JSON string
simple_public_company_dto_instance = SimplePublicCompanyDTO.from_json(json)
# print the JSON string representation of the object
print(SimplePublicCompanyDTO.to_json())

# convert the object into a dict
simple_public_company_dto_dict = simple_public_company_dto_instance.to_dict()
# create an instance of SimplePublicCompanyDTO from a dict
simple_public_company_dto_from_dict = SimplePublicCompanyDTO.from_dict(simple_public_company_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


