{
    "version": 2,
    "name": "notionApp",
    "builds": [
        {"src": "*.py", "use": "@now/python", "config": {"maxLambdaSize": "10mb"}}
    ]
}
