% rebase ('osnovna_stran.tpl', title = 'Sudoku')

<div class="tile is-ancestor">
    <div class="tile is-12">
        <div class="tile is-1"></div>
        <div class="tile is-6 notification is-primary">
            <div class="tile is-vertical">
                <p class="title">Pravila igre</p>
                <br>
                <p>V tabeli so vpisana števila od 1 do 9, nekaj polj pa je praznih. Cilj igre je, da izpolnete vsa prazna polja v tabeli
                tako, da se vsako število od 1 do 9 ponovi natanko enkrat v vsakem stolpcu, vsaki vrstici in vsaki manjši 3 x 3 mreži.</p>
                <br><p>Ob začetku nove igre boste najprej izbrali težavnost: višja kot je stopnja težavnosti, več praznih polj bo v križanki,
                da jih izpolnete sami.</p>
                <br><p>Da vpišete številko v tabelo, preprosto kliknite na prazno polje, vtipkajte številko med 1 in 9 ter 
                pritisnite <i>"Enter"</i>. Če boste vpisali pravilno številko, bo vpisovalno okence izginilo, če pa vpišete 
                napačno, se bo okence obarvalo rdeče.</p>
            </div>
        </div>
        <div class="tile is-1"></div>
        <div class="tile is-3">
            <div class="tile is-vertical">
                <br><br>
                <p>Če ste pripravljeni, izberite težavnost in že lahko začnete.</p><br>
                <p><b><i>Želim vam obilo zabave ob reševanju!</i></b></p><br>
                <form action = "/tezavnost/" method = "get">
                    <button type = "submit"  class="button is-rounded is-primary">Izberi težavnost</button>
                </form><br><br>
                <form action = "/" method = "get">
                    <button type = "submit"  class="button is-rounded is-danger">Nazaj na naslovno stran</button>
                </form>
            </div>
        </div>
        <div class="tile is-1"></div>
    </div>
</div>


