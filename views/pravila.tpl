% rebase ('osnovna_stran.tpl', title = 'Sudoku')

<h1>Pravila igre</h1>

<p>Če ste priprvljeni, izberite težavnost in že lahko začnete. Želim vam obilo zabave ob reševanju!</p>
<form action = "/tezavnost/" method = "get">
    <button type = "submit"  class="button is-rounded is-primary">Izberi težavnost</button>
</form>

<form action = "/" method = "get">
    <button type = "submit"  class="button is-rounded is-danger">Nazaj na naslovno stran</button>
</form>