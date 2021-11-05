import webbrowser

#Enter URL here
url = "https://www.youtube.com/watch?v=CGW_jkfA6wc"

download = url[:12] + "ss" +url[12:]
webbrowser.open(url)