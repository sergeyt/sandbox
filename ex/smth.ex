#!/usr/bin/env expect

if {$argc == 1} {
    set uid [lindex $argv 0]
} else {
    puts "usage: smth.ex <smth-id>"
    exit 1
}

set timeout 60
spawn luit -encoding gbk ssh $uid@newsmth.net
interact {
    timeout 290 { send "j$" }
}
