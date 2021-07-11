
# Youtube comment bot

this projects is develop with python for commenting to youtube videos

## Installation

```bash
pip install -r requirements.txt
```

## main.py
this files generate youtube links base on your keyword. I used [youtube search](https://pypi.org/project/youtube-search/) library to achieve that.

on line 5 of main.py you can add max-limit of the result you want

```python
results = YoutubeSearch(keyword, max_results=100).to_dict()
```

## bot.py
this's the main script for commenting on youtube videos.
On line 69 of bot.py you'll add the comment messages you wish.

```python
messages = [
		'I love python',
	 	'hello guys i\'m a python developer'
	]
```

on line 89, you get to add your google email and password linked to your youtube account
```python
    email = 'gmail@gmail.com'
	password = 'password'
```

## Note
Don't use this script for spaming youtube or else, youtube will ban your account


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/Josephchinedu/youtube-comment-bot/blob/main/LICENSE)