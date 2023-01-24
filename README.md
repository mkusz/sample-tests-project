

# Tworzenie nowego projektu

## Wstępna konfiguracja poetry

Zmieniamy domyślne ustawienie, aby poetry tworzyło wirtualne środowisko w podkatalogu projektu (domyślnie jest to podkatalog `.venv`).

```commandline
poetry config virtualenv.create true --local
```

## Nowy projekt w poetry

W katalogu projektu wykonujemy polecenie:

```commandline
poetry init
poetry env use python3.9  # lub inna wersja, której używacie
````

Wyklikujemy wszystko o co pyta nas instalator.

## Nowy projekt w poetry

Postępujemy podobnie jak w przypadku normalnego projektu, ale:

- Location - wskazujemy katalog, w którym utworzyliśmy nowy projekt poetry
- Previously configured interpreter -> Add interpreter -> Add local interpreter

Przy dodawaniu nowego interpretra wybieramy:

- Virtualenv Environment
- Existing -> ...
- Wskazujemy plik `python3` w podkatalogu `.venv/bin/` projektu (jeśli to windows to będzie `python3.exe`)
- Potwierdź przyciskiem `OK`

Potwierdzamy, że w oknie Interpreter jest poprawnie wybrana ścieżka do pliku Pythona i naciskamy `Create`. W kolejnym okienku wybieramy `Create from Existing Sources`

Po otwarciu okna `Terminal`, po lewej stronie będzie widać ścieżkę do wirutalnego środowiska (u mnie jest to `(sample-tests-project-py3.9) maq@cpu sample-test-project`).

# Poetry - instalacja pakietów

## Playwright

```commandline
poetry add playwright
poetry run playwright install chrome
poetry run playwright-deps chrome
```

## Pytet

```commandline
poetry add pytest
poetry add pytest_asyncio
```

## Pydantic i python-dotenv

Te 2 paczki, służą do obsługi m.in. zmiennych środowiskowych

```commandline
poetry add pydantic
poetry add python-dotenv
```
