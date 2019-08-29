% rebase ('osnovna_stran.tpl', title = 'Sudoku')

<h1>Sudoku</h1>

<p>Pozdravljeni!</p>
<p>Pred vami je sudoku, priljubljena logična igra, ki jo sestavlja tabela z devetimi stolpci in devetimi vrsticami.
V tabeli so vpisana števila od 1 do 9, nekaj polj pa je praznih. Cilj igre je, da izpolnete vsa prazna polja v tabeli
tako, da se vsako število od 1 do 9 ponovi natanko enkrat v vsakem stolpcu, vsaki vrstici in vsaki manjši 3 x 3 mreži.</p>
<p><i>razloži, kako se uporablja: kaj je kateri gumb, izberi težavnost itd....</i></p>

<form action = "/pravila/" method = "get">
    <button type = "submit">Pravila igre</button>
</form>


<p>Če ste priprvljeni, izberite težavnost in že lahko začnete. Želim vam obilo zabave ob reševanju!</p>

<form action = "/tezavnost/" method = "get">
    <button type = "submit">Izberi težavnost</button>
</form>