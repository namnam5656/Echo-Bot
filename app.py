from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    TemplateMessage,
    ButtonsTemplate,
    PostbackAction,
    FlexMessage,
    FlexContainer,
    QuickReply
)
from linebot.v3.webhooks import (
    MessageEvent,
    FollowEvent,
    PostbackEvent,
    TextMessageContent
)

import os
import json

app = Flask(__name__)

configuration = Configuration(access_token=os.getenv('CHANNEL_ACCESS_TOKEN'))
line_handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# Follow Event
@line_handler.add(FollowEvent)
def handle_follow(event):
    print(f'Got {event.type} event')

# Message Event
@line_handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    text = event.message.text
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        if text == 'flex-1':
            line_flex_json = {
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://nuoxinhealth.com/assets/images/class-01.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "iCAP傳統整復推拿初級技術員培訓班（試辦班）",
                            "wrap": True,
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "NT$39,800",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "全課程",
                                "wrap": True,
                                "weight": "bold",
                                "size": "sm",
                                "flex": 0,
                                "offsetStart": "5px"
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "action": {
                            "type": "uri",
                            "label": "點擊進行報名",
                            "uri": "https://nuoxinhealth.com/payment.html"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "查看培訓班的有關資訊",
                            "uri": "https://nuoxinhealth.com/class-01.html"
                            }
                        }
                        ]
                    }
                    },
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://nuoxinhealth.com/assets/images/class-02.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "禪柔團課 - 單堂",
                            "wrap": True,
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "flex": 1,
                            "contents": [
                            {
                                "type": "text",
                                "text": "NT$600",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "單堂",
                                "wrap": True,
                                "weight": "bold",
                                "size": "sm",
                                "flex": 0,
                                "offsetStart": "5px"
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "flex": 2,
                            "style": "primary",
                            "action": {
                            "type": "uri",
                            "label": "點擊進行報名",
                            "uri": "https://nuoxinhealth.com/payment.html"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "查看團課的有關資訊",
                            "uri": "https://nuoxinhealth.com/class-02.html"
                            }
                        }
                        ]
                    }
                    },
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://nuoxinhealth.com/assets/images/banner-2.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "禪柔團課 - 月課程(4堂)",
                            "wrap": True,
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "flex": 1,
                            "contents": [
                            {
                                "type": "text",
                                "text": "NT$2,000",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "月課程(4堂)",
                                "wrap": True,
                                "weight": "bold",
                                "size": "sm",
                                "flex": 0,
                                "offsetStart": "5px"
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "flex": 2,
                            "style": "primary",
                            "action": {
                            "type": "uri",
                            "label": "點擊進行報名",
                            "uri": "https://nuoxinhealth.com/payment.html"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "查看團課的有關資訊",
                            "uri": "https://nuoxinhealth.com/class-02.html"
                            }
                        }
                        ]
                    }
                    },
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://nuoxinhealth.com/assets/images/class-03.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "TRX懸吊訓練團課 - 單堂",
                            "wrap": True,
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "flex": 1,
                            "contents": [
                            {
                                "type": "text",
                                "text": "NT$2,000",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "單堂",
                                "wrap": True,
                                "weight": "bold",
                                "size": "sm",
                                "flex": 0,
                                "offsetStart": "5px"
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "flex": 2,
                            "style": "primary",
                            "action": {
                            "type": "uri",
                            "label": "點擊進行報名",
                            "uri": "https://nuoxinhealth.com/payment.html"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "查看團課的有關資訊",
                            "uri": "https://nuoxinhealth.com/class-03.html"
                            }
                        }
                        ]
                    }
                    },
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://nuoxinhealth.com/assets/images/banner-3.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "TRX懸吊訓練團課 - 課程(10堂)",
                            "wrap": True,
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "flex": 1,
                            "contents": [
                            {
                                "type": "text",
                                "text": "NT$18,000",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "課程(10堂)",
                                "wrap": True,
                                "weight": "bold",
                                "size": "sm",
                                "flex": 0,
                                "offsetStart": "5px"
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "flex": 2,
                            "style": "primary",
                            "action": {
                            "type": "uri",
                            "label": "點擊進行報名",
                            "uri": "https://nuoxinhealth.com/payment.html"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "查看團課的有關資訊",
                            "uri": "https://nuoxinhealth.com/class-03.html"
                            }
                        }
                        ]
                    }
                    },
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://nuoxinhealth.com/assets/images/class-04.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "高爾夫教學",
                            "wrap": True,
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "flex": 1,
                            "contents": [
                            {
                                "type": "text",
                                "text": "NT$9,000",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "10堂套課",
                                "wrap": True,
                                "weight": "bold",
                                "size": "sm",
                                "flex": 0,
                                "offsetStart": "5px"
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "flex": 2,
                            "style": "primary",
                            "action": {
                            "type": "uri",
                            "label": "點擊進行報名",
                            "uri": "https://nuoxinhealth.com/payment.html"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "查看教學的有關資訊",
                            "uri": "https://nuoxinhealth.com/class-04.html"
                            }
                        }
                        ]
                    }
                    },
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://nuoxinhealth.com/assets/images/class-05.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "皮拉提斯訓練課程 - 單堂",
                            "wrap": True,
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "flex": 1,
                            "contents": [
                            {
                                "type": "text",
                                "text": "NT$2,300",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "單堂",
                                "wrap": True,
                                "weight": "bold",
                                "size": "sm",
                                "flex": 0,
                                "offsetStart": "5px"
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "flex": 2,
                            "style": "primary",
                            "action": {
                            "type": "uri",
                            "label": "點擊進行報名",
                            "uri": "https://nuoxinhealth.com/payment.html"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "查看課程的有關資訊",
                            "uri": "https://nuoxinhealth.com/class-05.html"
                            }
                        }
                        ]
                    }
                    },
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://nuoxinhealth.com/assets/images/banner-1.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "皮拉提斯訓練課程 - 月課程(4堂)",
                            "wrap": True,
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "flex": 1,
                            "contents": [
                            {
                                "type": "text",
                                "text": "NT$9,500",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "月課程(4堂)",
                                "wrap": True,
                                "weight": "bold",
                                "size": "sm",
                                "flex": 0,
                                "offsetStart": "5px"
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "flex": 2,
                            "style": "primary",
                            "action": {
                            "type": "uri",
                            "label": "點擊進行報名",
                            "uri": "https://nuoxinhealth.com/payment.html"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "查看課程的有關資訊",
                            "uri": "https://nuoxinhealth.com/class-05.html"
                            }
                        }
                        ]
                    }
                    }
                ]
                }
        
        elif text == '課程':
            line_flex_json = {
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://nuoxinhealth.com/assets/images/class-01.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "iCAP傳統整復推拿初級技術員培訓班（試辦班）",
                            "wrap": True,
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "NT$39,800",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "全課程",
                                "wrap": True,
                                "weight": "bold",
                                "size": "sm",
                                "flex": 0,
                                "offsetStart": "5px"
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "action": {
                            "type": "uri",
                            "label": "點擊進行報名",
                            "uri": "https://nuoxinhealth.com/payment.html"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "查看培訓班的有關資訊",
                            "uri": "https://nuoxinhealth.com/class-01.html"
                            }
                        }
                        ]
                    }
                    },
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://nuoxinhealth.com/assets/images/class-02.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "禪柔團課 - 單堂",
                            "wrap": True,
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "flex": 1,
                            "contents": [
                            {
                                "type": "text",
                                "text": "NT$600",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "單堂",
                                "wrap": True,
                                "weight": "bold",
                                "size": "sm",
                                "flex": 0,
                                "offsetStart": "5px"
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "flex": 2,
                            "style": "primary",
                            "action": {
                            "type": "uri",
                            "label": "點擊進行報名",
                            "uri": "https://nuoxinhealth.com/payment.html"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "查看團課的有關資訊",
                            "uri": "https://nuoxinhealth.com/class-02.html"
                            }
                        }
                        ]
                    }
                    },
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://nuoxinhealth.com/assets/images/banner-2.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "禪柔團課 - 月課程(4堂)",
                            "wrap": True,
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "flex": 1,
                            "contents": [
                            {
                                "type": "text",
                                "text": "NT$2,000",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "月課程(4堂)",
                                "wrap": True,
                                "weight": "bold",
                                "size": "sm",
                                "flex": 0,
                                "offsetStart": "5px"
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "flex": 2,
                            "style": "primary",
                            "action": {
                            "type": "uri",
                            "label": "點擊進行報名",
                            "uri": "https://nuoxinhealth.com/payment.html"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "查看團課的有關資訊",
                            "uri": "https://nuoxinhealth.com/class-02.html"
                            }
                        }
                        ]
                    }
                    },
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://nuoxinhealth.com/assets/images/class-03.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "TRX懸吊訓練團課 - 單堂",
                            "wrap": True,
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "flex": 1,
                            "contents": [
                            {
                                "type": "text",
                                "text": "NT$2,000",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "單堂",
                                "wrap": True,
                                "weight": "bold",
                                "size": "sm",
                                "flex": 0,
                                "offsetStart": "5px"
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "flex": 2,
                            "style": "primary",
                            "action": {
                            "type": "uri",
                            "label": "點擊進行報名",
                            "uri": "https://nuoxinhealth.com/payment.html"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "查看團課的有關資訊",
                            "uri": "https://nuoxinhealth.com/class-03.html"
                            }
                        }
                        ]
                    }
                    },
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://nuoxinhealth.com/assets/images/banner-3.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "TRX懸吊訓練團課 - 課程(10堂)",
                            "wrap": True,
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "flex": 1,
                            "contents": [
                            {
                                "type": "text",
                                "text": "NT$18,000",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "課程(10堂)",
                                "wrap": True,
                                "weight": "bold",
                                "size": "sm",
                                "flex": 0,
                                "offsetStart": "5px"
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "flex": 2,
                            "style": "primary",
                            "action": {
                            "type": "uri",
                            "label": "點擊進行報名",
                            "uri": "https://nuoxinhealth.com/payment.html"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "查看團課的有關資訊",
                            "uri": "https://nuoxinhealth.com/class-03.html"
                            }
                        }
                        ]
                    }
                    },
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://nuoxinhealth.com/assets/images/class-04.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "高爾夫教學",
                            "wrap": True,
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "flex": 1,
                            "contents": [
                            {
                                "type": "text",
                                "text": "NT$9,000",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "10堂套課",
                                "wrap": True,
                                "weight": "bold",
                                "size": "sm",
                                "flex": 0,
                                "offsetStart": "5px"
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "flex": 2,
                            "style": "primary",
                            "action": {
                            "type": "uri",
                            "label": "點擊進行報名",
                            "uri": "https://nuoxinhealth.com/payment.html"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "查看教學的有關資訊",
                            "uri": "https://nuoxinhealth.com/class-04.html"
                            }
                        }
                        ]
                    }
                    },
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://nuoxinhealth.com/assets/images/class-05.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "皮拉提斯訓練課程 - 單堂",
                            "wrap": True,
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "flex": 1,
                            "contents": [
                            {
                                "type": "text",
                                "text": "NT$2,300",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "單堂",
                                "wrap": True,
                                "weight": "bold",
                                "size": "sm",
                                "flex": 0,
                                "offsetStart": "5px"
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "flex": 2,
                            "style": "primary",
                            "action": {
                            "type": "uri",
                            "label": "點擊進行報名",
                            "uri": "https://nuoxinhealth.com/payment.html"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "查看課程的有關資訊",
                            "uri": "https://nuoxinhealth.com/class-05.html"
                            }
                        }
                        ]
                    }
                    },
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "url": "https://nuoxinhealth.com/assets/images/banner-1.jpg"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "皮拉提斯訓練課程 - 月課程(4堂)",
                            "wrap": True,
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "flex": 1,
                            "contents": [
                            {
                                "type": "text",
                                "text": "NT$9,500",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "月課程(4堂)",
                                "wrap": True,
                                "weight": "bold",
                                "size": "sm",
                                "flex": 0,
                                "offsetStart": "5px"
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "flex": 2,
                            "style": "primary",
                            "action": {
                            "type": "uri",
                            "label": "點擊進行報名",
                            "uri": "https://nuoxinhealth.com/payment.html"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "查看課程的有關資訊",
                            "uri": "https://nuoxinhealth.com/class-05.html"
                            }
                        }
                        ]
                    }
                    }
                ]
                }
            line_flex_str = json.dumps(line_flex_json)
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        FlexMessage(
                            alt_text='Flex Message',
                            contents=FlexContainer.from_json(line_flex_str))]
                )
            )

if __name__ == "__main__":
    app.run()