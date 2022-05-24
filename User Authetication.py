from requests import request
import requests
import requests.auth


client_auth = requests.auth.HTTPBasicAuth('p-yMDWbffUu3VkHWaBzBztQA', 'IaFIqNQJUSHiwfoOrK3erM1Vy2YslQ')
post_data = {"grant_type": "password", "username": "Jadyin", "password": "Dovah8320"}
headers = {"User-Agent": "ChangeMeClient/0.1 by Jadyin"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
response.json()
{u'access_token': u'fhTdafZI-0ClEzzYORfBSCR7x3M',
 u'expires_in': 3600,
 u'scope': u'*',
 u'token_type': u'bearer'}
headers = {"Authorization": "bearer fhTdafZI-0ClEzzYORfBSCR7x3M", "User-Agent": "ChangeMeClient/0.1 by Jadyin"}
esponse = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
response.json()
{u'comment_karma': 0,
 u'created': 1389649907.0,
 u'created_utc': 1389649907.0,
 u'has_mail': False,
 u'has_mod_mail': False,
 u'has_verified_email': None,
 u'id': u'1',
 u'is_gold': False,
 u'is_mod': True,
 u'link_karma': 1,
 u'name': u'reddit_bot',
 u'over_18': True}