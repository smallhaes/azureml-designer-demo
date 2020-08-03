# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .ui_column_picker import UIColumnPicker


class UIParameterHintColumnPicker(UIColumnPicker):
    """UIParameterHintColumnPicker.

    :param column_picker_for:
    :type column_picker_for: str
    :param column_selection_categories:
    :type column_selection_categories: list[str]
    :param single_column_selection:
    :type single_column_selection: bool
    """

    _attribute_map = {
        'column_picker_for': {'key': 'columnPickerFor', 'type': 'str'},
        'column_selection_categories': {'key': 'columnSelectionCategories', 'type': '[str]'},
        'single_column_selection': {'key': 'singleColumnSelection', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(UIParameterHintColumnPicker, self).__init__(**kwargs)