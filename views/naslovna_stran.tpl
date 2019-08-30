% rebase ('osnovna_stran.tpl', title = 'Sudoku')


<div class="tile is-ancestor">
    <div class="tile is-12">
        <div class="tile is-1"></div>
        <div class="tile is-4 notification is-primary">
            <div class="tile is-vertical">
                <p class="title">Sudoku</p>
                <br>
                <p class="subtitle">Pozdravljeni!</p>
                <p>Pred vami je sudoku, priljubljena logična igra, ki jo sestavlja tabela z devetimi stolpci in devetimi vrsticami.
                Sudoku je sestavil Howard Garns, upokojen arhitekt in sestavljavec križank, in ga prvič objavil leta 1979, na Japonskem
                pa je bil sudoku prvič predstavljen v reviji Monthly Nikolist leta 1984. Danes je sudoku znan po vsem svetu in je zelo
                priljubljena igra tako pri otrocih kot pri odraslih.</p>
            </div>
        </div>
        <div class="tile is-3 notification is-danger">
            <div class="tile is-vertical">
                <p class="subtitle">Igrate prvič?</p><br>
                <p>Bolje spoznajte pravila sudokuja:</p>
                <br><br>
                <form action = "/pravila/" method = "get">
                    <button type = "submit" class="button is-rounded">Pravila igre</button>
                </form>
            </div>
        </div>
        <div class="tile is-3 notification is-primary">
            <div class="tile is-vertical">
                <p class="subtitle">Pa začnimo...</p><br>
                <p>Če ste pripravljeni, izberite težavnost in že lahko začnete. <br><br><b><i>Želim vam obilo zabave ob reševanju!</i></b></p>
                <br>
                <form action = "/tezavnost/" method = "get">
                    <button type = "submit" class="button is-rounded ">Izberi težavnost</button>
                </form>
            </div>
        </div>
        <div class="tile is-1"></div>
    </div>
</div>