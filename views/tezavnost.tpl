% rebase ('osnovna_stran.tpl', title = 'Sudoku')

<div class="tile is-ancestor">
    <div class="tile is-12">
        <div class="tile is-1"></div>
        <div class="tile is-6 is-vertical notification is-primary">
            <p class="title">Težavnost</p>
            <br>
            <p>Različne tabele sudoku se razlikujejo po težavnosti. Pri tem višja stopnja
            težavnosti pomeni več praznih polj, v katera vpisujete števila. Izberete lahko 
            med tremi možnostmi:<br><br>
            <center><ul>
                <li><i>lahko</i> (20 praznih polj), </li>
                <li><i>srednje težko</i> (40 praznih polj) in</li>
                <li><i>težko</i> (60 praznih polj).</li>
            </ul></center>
            </p>
        </div>
        <div class="tile is-1"></div>
        <div class="tile is-5  is-vertical">
            <br><p>Izberite težavnost in že lahko začnete:</p><br>
            <div class="field is-grouped">
                <p class="control">
                    <form action = "/tezavnost1/" method = "post">
                            <button type = "submit"  class="button is-rounded is-primary">Lahko</button>
                    </form>
                </p>
                <p class="control">
                    <form action = "/tezavnost2/" method = "post">
                        <button type = "submit"  class="button is-rounded is-primary">Srednje težko</button>
                    </form>
                </p>
                <p class="control">
                    <form action = "/tezavnost3/" method = "post">
                        <button type = "submit"  class="button is-rounded is-primary">Težko</button>
                    </form>
                </p>
            </div><br><br>
            <form action = "/" method = "get">
                <button type = "submit"  class="button is-rounded is-danger">Nazaj na naslovno stran</button>
            </form>
            
        </div>
    </div>
</div>











