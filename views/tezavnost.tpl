% rebase ('osnova.tpl', title = 'Sudoku')

<h1>Težavnost</h1>

<p>Različne tabele sudoku se razlikujejo po težavnosti. Izberite težavnost:</p>
<form action = "/tezavnost1/" method = "post">
    <button type = "submit">Lahko</button>
</form>
<form action = "/tezavnost2/" method = "post">
    <button type = "submit">Srednje težko</button>
</form>
<form action = "/tezavnost3/" method = "post">
    <button type = "submit">Težko</button>
</form>




<form action = "/" method = "get">
    <button type = "submit">Nazaj na naslovno stran</button>
</form>