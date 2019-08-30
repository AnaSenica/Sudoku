% rebase ('osnovna_stran.tpl', title = 'Sudoku')
<div class="tile is-ancestor">
    <div class="tile is-12">
        <div class="tile is-3"></div>
        <div class="tile is-6 is-vertical">
            <article class="message is-danger">
                <div class="message-header">
                    <p>Pozor!</p>
                </div>
                <div class="message-body">
                    <p>Vtipkati morate številko <strong>med 1 in 9</strong>!</p>
                </div>
                <div align ='center'>
                    <form action = "/igra/" method = "get">
                        <button type = "submit" class="button is-rounded">Nazaj</button>
                    </form>
                    <br>
                </div>
            </article>
        </div>
        <div class="tile is-3"></div>
    </div>
</div>




