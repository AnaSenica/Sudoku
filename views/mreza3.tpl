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
            <form action = "/igra/"  method = "post" >
                <input name = "stevilo" size="3">
                <input type = "hidden" name="vrsta" value="{{vrsta}}">
                <input type = "hidden" name="stolpec" value="{{stolpec}}">
            </form>
        </td>
        %else:
        <td>
            % if stevilo != polna[vrsta][stolpec]:
            <font color="red">{{stevilo}}</font>
            <form action = "/igra/"  method = "post" >
                <input name = "stevilo" size="3">
                <input type = "hidden" name="vrsta" value="{{vrsta}}">
                <input type = "hidden" name="stolpec" value="{{stolpec}}">
            </form>
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
            <form action = "/igra/"  method = "post" >
                <input name = "stevilo" size="3">
                <input type = "hidden" name="vrsta" value="{{vrsta}}">
                <input type = "hidden" name="stolpec" value="{{stolpec}}">
            </form>
        </td>
        %else:
        <td>
            % if stevilo != polna[vrsta][stolpec]:
            <form action = "/igra/"  method = "post" >
                <input name = "stevilo" size="3">
                <input type = "hidden" name="vrsta" value="{{vrsta}}">
                <input type = "hidden" name="stolpec" value="{{stolpec}}">
            </form>
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
            <form action = "/igra/"  method = "post" >
                <input name = "stevilo" size="3">
                <input type = "hidden" name="vrsta" value="{{vrsta}}">
                <input type = "hidden" name="stolpec" value="{{stolpec}}">
            </form>
        </td>
        %else:
        <td>
            % if stevilo != polna[vrsta][stolpec]:
            <font color="red">{{stevilo}}</font>
            <form action = "/igra/"  method = "post" >
                <input name = "stevilo" size="3">
                <input type = "hidden" name="vrsta" value="{{vrsta}}">
                <input type = "hidden" name="stolpec" value="{{stolpec}}">
            </form>
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
            <form action = "/igra/"  method = "post" >
                <input name = "stevilo" size="3">
                <input type = "hidden" name="vrsta" value="{{vrsta}}">
                <input type = "hidden" name="stolpec" value="{{stolpec}}">
            </form>
        </td>
        %else:
        <td>
            % if stevilo != polna[vrsta][stolpec]:
            <font color="red">{{stevilo}}</font>
            <form action = "/igra/"  method = "post" >
                <input name = "stevilo" size="3">
                <input type = "hidden" name="vrsta" value="{{vrsta}}">
                <input type = "hidden" name="stolpec" value="{{stolpec}}">
            </form>
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