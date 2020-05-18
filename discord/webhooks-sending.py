import requests
url = "https://example.com/youHaveToReplaceThisLinkWithYourWebhookURL"

des = """Lorem ipsum dolor sit amet 🤣💩, consectetur adipiscing elit. Nullam ornare blandit mollis. Pellentesque a augue vehicula, aliquet tortor in, sodales felis. Lorem ipsum dolor sit amet, consectetur adipiscing elit."""

r = requests.post(url, json = {
    "embeds":[
        {
            "title":"New Facebook post!",
            "color":"4351922",
            "description":des,
            "thumbnail":{"url":"https://szymonbednorz.com/img/fb.png"},
            "image":{"url":"https://szymonbednorz.com/img/dsonyy.png"},
            "footer":{"text":"dsonyy"},
            "author":{"name":"@dsonyy"},
            "url":"https://szymonbednorz.com/"
        }
    ]
})
r.raise_for_status()
