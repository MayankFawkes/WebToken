# WebToken
A program which create encrypted token for client server talk. Requests validation.

# Use
Client will generate encrypted token and server will validate the token which is valid for 15 second DEFAULT
You can increase token valid time in Server.py
```
if __name__ == '__main__':
	second=15   # time in second to increase hash valid time
	while True:
		try:
			st=input('Enter Hash -->')
			if check(st.split('-')):
				print('Success')
			else:
				print('Error')
		except:
			print('Error')
```
# Contribute 
Anyone can freely contribute converting client script into javascript

## Author

- [Mayank Gupta](https://github.com/MayankFawkes)

## LICENSE

[MIT License](https://github.com/MayankFawkes/WebToken/blob/master/LICENSE)

NOTE: Send me some feedback to make this project more powerfull than ever! <3
