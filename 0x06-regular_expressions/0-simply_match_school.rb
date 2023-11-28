#!/usr/bin/env ruby

if ARGV.empty?
  puts 'Usage: ./script_name.rb <input>'
  exit 1
end

input = Regexp.escape(ARGV[0])
puts input.scan(/School/i).join
