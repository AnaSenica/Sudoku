% rebase ('osnovna_stran.tpl', title = 'Sudoku')
<article class="message is-danger">
    <div class="message-header">
          <p>Pozor!</p>
    </div>
    <div class="message-body">
          Vtipkati morate številko <strong>med 1 in 9</strong>!
    </div>
    <div align ='center'>
        <form action = "/igra/" method = "get">
            <button type = "submit" class="button is-rounded">Nazaj</button>
        </form>
    </div>
    <div>
            <br>
    </div>
</article>
