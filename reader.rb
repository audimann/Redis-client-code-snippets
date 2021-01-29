#!/usr/bin/ruby

require "redis" 

passwd = CGI.escape("<your_redis_password>")
redis_handle = Redis.new(url: "redis://:#{passwd}@<your_redis_host>:<your_redis_port>")

numList = (redis_handle.lrange("numKey",0,-1)).map(&:to_i)
puts numList.sort.reverse.join(' ')
