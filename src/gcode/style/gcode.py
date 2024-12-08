style = """
#gcode_widget_control,#gcode_main,#gcode_widget_code {
    padding: 0px; 
    border: none !important;
}

#gcode_main {
    background-color: blue;
}

#gcode_widget_code {
    background-color: #EFEFEF;
}

#gcode_widget_control {
    background-color: #EFEFEF;
}

#gcode_widget_filter {
    background-color: #D9D9D9;
    border: node !important;
    border-radius: 5px;
}

#gcode_text_edit_line_number,#gcode_text_edit_code,#gcode_filter_label_search{
    padding: 5px;  
    color: #343434;
    font-family: Inter;
    font-size: 12px;
    line-height: 200%;
}

#gcode_filter_label_search,#gcode_button_open_file {  
    padding: 0px;   
    font-size: 8px;
    color: #000000;
}

#gcode_filter_line_edit {  
    background-color: #FFFFFF; 
    border: node !important;
    border-radius: 5px;
    padding: 5px;   
    font-size: 8px;
    color: #000000;
}

#gcode_text_edit_line_number,#gcode_button_open_file {
    background-color: #D9D9D9;   
    border: node !important;
    border-radius: 5px;
}

#gcode_text_edit_code {
    background-color: #EFEFEF;  
    border: none !important;
}

#gcode_button_drive {
    border-image: url(src/gcode/icon/drive_icon_deactivated.svg);
}

#gcode_button_drive:checked {
    border-image: url(src/gcode/icon/drive_icon_activated.svg);
}

#gcode_button_filter {
    border-image: url(src/gcode/icon/filter_icon_deactivated.svg);
}

#gcode_button_filter:checked {
    border-image: url(src/gcode/icon/filter_icon_activated.svg);
}

#gcode_button_open_file {
    text-align: left;
    padding-left: 8px;
}
"""