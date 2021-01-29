# Redis-client-code-snippets
Small sample code snippets in Python and Ruby to connect, read nd write data from a Redis server/cluster

## Requirements
Python and/or Ruby must be installed to execute the scripts 

```bash
apt-get install python
apt-get install python3
apt-get install ruby
```

For python, the **redis** package needs to be installed (e.g. via pip). For Ruby, the **redis** gem needs to be installed:
```bash
pip install redis
pip3 install redis
gem install redis
```

## Usage
The python code **writer.py** and the ruby code **reader.rb** need to be adjusted for your environment:
- The hostname or IP address to connect to (i.e. where your Redis server is running)
- The Port number where the Redis server is listening to
- The password which protects the database needs to specified
```python
redis_handle = redis.Redis( host='<your_redis_host>', port=<your_redis_port>, password='<your_redis_password>')
```
```ruby
passwd = CGI.escape("<your_redis_password>")
redis_handle = Redis.new(url: "redis://:#{passwd}@<your_redis_host>:<your_redis_port>")
```
The 'writer.py' code inserts a list of 100 integer values (starting with 1, incrementing by 1) as a value to a key called **numKey**. Redis stores the integer values as strings. The 'reader.rb' code is reading these 100 numbers and printing them as integers in reverse order. To run the scripts:

```bash
python writer.py
python3 writer.py
./reader.rb
```

## Platforms Tested
In its initial release, the snippets were only tested on:
- Ubuntu 18.04 with Python 2.7.17
- Ubuntu 18.04 with Python 3.6.9
- Ubuntu 18.04 with Ruby 2.5.1

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors and acknowledgment
Michael Ehrig (michael.ehrig@email.de)
