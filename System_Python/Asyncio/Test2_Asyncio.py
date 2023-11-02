from random import randint
import asyncio
import webbrowser

MAX_POKEMON = 898

def open_url(url: str, google_chrome=False) -> None:
    if google_chrome:
        chrome_path = r"open -a Google\ Chrome %s"
        webbrowser.get(chrome_path).open(url)
    else:
        webbrowser.open(url)

def random_pokemon(google_chrome=False) -> str:
    pokemon_id = randint(0, MAX_POKEMON)
    pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    open_url(pokemon_url, google_chrome)

def main():
    return 0

if __name__ == '__main__':
    # asyncio.run(main())
    main()

