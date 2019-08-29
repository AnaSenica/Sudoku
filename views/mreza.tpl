% rebase ('osnovna_stran.tpl', title = 'Sudoku')

<div class="tile is-ancestor">
    <div class="tile"></div>
    <div class="tile">


<p align ='center'>
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
        <td width = "36px" height = "36px"  style="text-align: center; vertical-align: middle;">
            <form action = "/igra/"  method = "post" >
                <input name = "stevilo" class="input is-primary" style="width: 35px; height: 35px" autocomplete="off">
                <input type = "hidden" name="vrsta" value="{{vrsta}}">
                <input type = "hidden" name="stolpec" value="{{stolpec}}">
            </form>
        </td>
        %else:
        <td width = "36px" height = "36px" style="text-align: center; vertical-align: middle;">
            % if stevilo != polna[vrsta][stolpec]:
            <form action = "/igra/"  method = "post" >
                <input name = "stevilo" class="input is-danger" placeholder="{{stevilo}}" style="width: 35px; height: 35px" autocomplete="off">
                <input type = "hidden" name="vrsta" value="{{vrsta}}">
                <input type = "hidden" name="stolpec" value="{{stolpec}}">
            </form>
            % else:
            {{stevilo}}
            %end
        </td>
        %end
        <td width = "0.5"></td>
        

        %else:
        %stevilo = sudoku[vrsta][stolpec]
        %if stevilo == '_':
        <td width = "36px" height = "36px"  style="text-align: center; vertical-align: middle;">
            <form action = "/igra/"  method = "post" >
                <input name = "stevilo" class="input is-primary" style="width: 35px; height: 35px" autocomplete="off">
                <input type = "hidden" name="vrsta" value="{{vrsta}}">
                <input type = "hidden" name="stolpec" value="{{stolpec}}">
            </form>
        </td>
        %else:
        <td width = "36px" height = "36px" style="text-align: center; vertical-align: middle;"> 
            % if stevilo != polna[vrsta][stolpec]:
            <form action = "/igra/"  method = "post" >
                <input name = "stevilo" class="input is-danger" placeholder="{{stevilo}}" style="width: 35px; height: 35px" autocomplete="off">
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
        <td width = "36px" height = "36px" style="text-align: center; vertical-align: middle;">
            <form action = "/igra/"  method = "post" >
                <input name = "stevilo" class="input is-primary" style="width: 35px; height: 35px" autocomplete="off">
                <input type = "hidden" name="vrsta" value="{{vrsta}}">
                <input type = "hidden" name="stolpec" value="{{stolpec}}">
            </form>
        </td>
        %else:
        <td width = "36px" height = "36px" style="text-align: center; vertical-align: middle;">
            % if stevilo != polna[vrsta][stolpec]:
            <form action = "/igra/"  method = "post" >
                <input name = "stevilo" class="input is-danger" placeholder="{{stevilo}}" style="width: 35px; height: 35px" autocomplete="off">
                <input type = "hidden" name="vrsta" value="{{vrsta}}">
                <input type = "hidden" name="stolpec" value="{{stolpec}}">
            </form>
            % else:
            {{stevilo}}
            %end
        </td>
        %end
        <td width = "0.5"></td>
            
    
        %else:
        %stevilo = sudoku[vrsta][stolpec]
        %if stevilo == '_':
        <td width = "36px" height = "36px" style="text-align: center; vertical-align: middle;">
            <form action = "/igra/"  method = "post" >
                <input name = "stevilo" class="input is-primary" style="width: 35px; height: 35px" autocomplete="off">
                <input type = "hidden" name="vrsta" value="{{vrsta}}">
                <input type = "hidden" name="stolpec" value="{{stolpec}}">
            </form>
        </td>
        %else:
        <td width = "36px" height = "36px" style="text-align: center; vertical-align: middle;">
            % if stevilo != polna[vrsta][stolpec]:
            <form action = "/igra/"  method = "post" >
                <input name = "stevilo" class="input is-danger" placeholder="{{stevilo}}" style="width: 35px; height: 35px" autocomplete="off">
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
</p>


</div>
<div class="tile"></div>
</div>