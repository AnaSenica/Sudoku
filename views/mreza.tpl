% rebase ('osnova.tpl', title = 'Sudoku')

<table border="1">
    %sudoku = igra.sudoku
    %for vrsta in range(9):
    <tr>
        %for stolpec in range(9):
        %stevilo = sudoku[vrsta][stolpec]
        %if stevilo == '_':
        <td>
            <form action = "/igra/" method = "post">
                <input name = "stevilo">
            </form>
        </td>
        %else:
        <td>
            {{stevilo}}
        </td>
        %end
        %end
    </tr>
    
    %end

</table>

