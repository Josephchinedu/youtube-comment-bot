from youtube_search import YoutubeSearch
import webbrowser

keyword = str(input("Put your Keyword:"))
results = YoutubeSearch(keyword, max_results=100).to_dict()
for v in results:
    newhref = 'https://www.youtube.com' + v['url_suffix'] + '\n'
    f = open('url.txt', "a")
    f.write(newhref)
    f.close()
    print('https://www.youtube.com' + v['url_suffix'])