% rebase ('osnovna_stran.tpl', title = 'Sudoku')


<div class="tile is-ancestor">
    <div class="tile is-12">
        <div class="tile is-6">
            <div class="tile is-vertical">
                    <p class="title">Sudoku</p>

                    <br>
                    <p class="subtitle">Pozdravljeni!</p>

                    <p>Pred vami je sudoku, priljubljena logična igra, ki jo sestavlja tabela z devetimi stolpci in devetimi vrsticami.
                    V tabeli so vpisana števila od 1 do 9, nekaj polj pa je praznih. Cilj igre je, da izpolnete vsa prazna polja v tabeli
                    tako, da se vsako število od 1 do 9 ponovi natanko enkrat v vsakem stolpcu, vsaki vrstici in vsaki manjši 3 x 3 mreži.</p>
                    <p><i>razloži, kako se uporablja: kaj je kateri gumb, izberi težavnost itd....</i></p>
            </div>
        </div>
        <div class="tile is-3">
                    <form action = "/pravila/" method = "get">
                        <button type = "submit" class="button is-rounded is-primary">Pravila igre</button>
                    </form>
        </div>
        <div class="tile is-3">
            <div class="tile is-vertical">
                    <p>Če ste priprvljeni, izberite težavnost in že lahko začnete. Želim vam obilo zabave ob reševanju!</p>
                    <form action = "/tezavnost/" method = "get">
                        <button type = "submit" class="button is-rounded is-primary">Izberi težavnost</button>
                    </form>
            </div>
        </div>
    </div>
</div>