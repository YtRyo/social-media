import requests, time, sys, json

# AuthorBy: RyoDev
# Facebook: bit.ly/YtRyoFb
# Instagram: bit.ly/YtRyoIg
# Wesite: bit.ly/YtRyoWeb

# Enter the API token here | Get API token at https://afara.my.id
Token = 'En7oT0NDqRS19Qb8OXtHwdMt0aLihV'

def login():
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Authorization": "Bearer " + Token
    }
    user = requests.get('https://afara.my.id/api/user', headers = headers).json()
    return user



def main():
    user = login()

    if 'message'in user:
        print('Invalid API token, get API token at "https://afara.my.id"')
    else:
        print('Name:', user['data']['name'])
        print('Email:', user['data']['email'])
        print("""
        1. Ambil Link Video Facebook
        2. Ambil Link Video Youtube

        99. Exit
        """)
        x = input('Chose: ')
        if x == '1':
            facebookGetLinks()
        else:
            if x == '2':
                YoutubeGetLinks()
            else:
                if x == '99':
                    print('Exit.')
                    sys.exit()
                else:
                    print('Choice does not exist.')
                    main()



def YoutubeGetLinks():
    url = input('Enter URl: ')

    res = requests.get('https://afara.my.id/api/get-youtube-video-link', data = '{"url": "'+ url +'"}', headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Authorization": "Bearer " + Token
    }).json()

    if 'error' in res:
        print(res['error'])
        x = input('1.Main menu, 2.Try again or enter to Exit: ')
        if x == '1':
            main()
        elif x == '2':
            YoutubeGetLinks()
        else:
            sys.exit()
    else:
        print('Title:', res['data']['title'])
        print('Type:', res['data']['type'])
        print('Thumbnail:', res['data']['thumbnail_url'])
        
        print('')
        for url in res['data']['urls']:
            print('Format:', url['format'])
            print('URl:', url['url'])
            print('=====================')
        
        print('')
    
    x = input('1.Main menu, 2.Try again or enter to Exit: ')
    if x == '1':
        main()
    elif x == '2':
        YoutubeGetLinks()
    else:
        sys.exit()



def facebookGetLinks():
    url = input('Enter URl: ')
    
    res = requests.get('https://afara.my.id/api/get-facebook-video-link', data = '{"url": "'+ url +'"}', headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Authorization": "Bearer " + Token
    }).json()

    if 'error' in res:
        print(res['error'])
        x = input('1.Main menu, 2.Try again or enter to Exit: ')
        if x == '1':
            main()
        elif x == '2':
            facebookGetLinks()
        else:
            sys.exit()
    else:
        print('')
        print('Kualitas SD:', res['sd_link'])
        print('Kualitas HD:', res['hd_link'])
        print('')

    x = input('1.Main menu, 2.Try again or enter to Exit: ')
    if x == '1':
        main()
    elif x == '2':
        facebookGetLinks()
    else:
        sys.exit()



if __name__ == "__main__":
    main()