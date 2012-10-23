#!/bin/bash
#
# This cron job reports you the partition which has used over its 80% capacity,
# can you shorten it more?
#
# MAILTO=you@example.com
# 0 13 * * * df -hl | awk 'int($5) > 80'

df -hl | awk 'int($5) > 80'
