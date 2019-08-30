% rebase ('osnovna_stran.tpl', title = 'Sudoku')

<div class="tile is-ancestor">
        <div class="tile is-12">
            <div class="tile is-3"></div>
            <div class="tile is-6 is-vertical">
                <article class="message is-danger">
                    <div class="message-header">
                        <p>Čestitam, zmagali ste!</p>
                    </div>
                    <div class="message-body">
                        <p>Želite igrati še enkrat?</p>
                    </div>
                    <div align ='center'>
                        <form action = "/" method = "get">
                            <button type = "submit" class="button is-rounded">Naslovna stran</button>
                        </form>
                        <br>
                    </div>
                </article>
            </div>
            <div class="tile is-3"></div>
        </div>
    </div>
    



