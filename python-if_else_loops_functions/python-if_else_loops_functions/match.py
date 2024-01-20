#!/usr/bin/python3
def http_error(status):
	case 400:
		return "bad request"
	case 404:
		return "not found"
	case 418:
		return "I am a tea pot"
	case _:
		return "something wrong with the internet"

