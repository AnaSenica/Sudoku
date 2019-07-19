% rebase ('osnova.tpl', title = 'Sudoku')

<table border>
    %sudoku = igra.sudoku
    %polna = igra.polna
    %for vrsta in range(9):
    %if vrsta == 2 or vrsta == 5:
    <tr>
        %for stolpec in range(9):
        %if stolpec == 2 or stolpec == 5:
        %stevilo = sudoku[vrsta][stolpec]

        %if stevilo == '_':
        <td>
        </td>
        %else:
        <td>
            % if stevilo != polna[vrsta][stolpec]:
            <font color="red">{{stevilo}}</font>
            % else:
            {{stevilo}}
            %end
        </td>
        %end
        <td></td>
        

        %else:
        %stevilo = sudoku[vrsta][stolpec]
        %if stevilo == '_':
        <td>
        </td>
        %else:
        <td>
            % if stevilo != polna[vrsta][stolpec]:
            <font color="red">{{stevilo}}</font>
            % else:
            {{stevilo}}
            %end
        </td>
        %end
        %end
        %end
    </tr>

    <tr>
        <td colspan="11"></td>
    </tr>
    %else:
    <tr>
        %for stolpec in range(9):
        %if stolpec == 2 or stolpec == 5:
        %stevilo = sudoku[vrsta][stolpec]
    
        %if stevilo == '_':
        <td>
        </td>
        %else:
        <td>
            % if stevilo != polna[vrsta][stolpec]:
            <font color="red">{{stevilo}}</font>
            % else:
            {{stevilo}}
            %end
        </td>
        %end
        <td></td>
            
    
        %else:
        %stevilo = sudoku[vrsta][stolpec]
        %if stevilo == '_':
        <td>
        </td>
        %else:
        <td>
            % if stevilo != polna[vrsta][stolpec]:
            <font color="red">{{stevilo}}</font>
            % else:
            {{stevilo}}
            %end
        </td>
        %end
        %end
        %end
    </tr>
    %end

    %end

</table>

<form action = "/igra/" method = "post">
    <label for="stevilo">Število:</label>
    <input name="stevilo">
    <label for="vrsta">Vrsta:</label>
    <input name="vrsta">
    <label for="stolpec">Stolpec:</label>
    <input name="stolpec">
    <button type = "submit">Ugibaj</button>
</form>