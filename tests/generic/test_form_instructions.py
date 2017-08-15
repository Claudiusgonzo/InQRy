from inqry import barcode
from inqry import form_instructions

instructions = form_instructions.FormInstructions()


def test_barcode_data_delayify():
    assert barcode.delayify('foo') == '~dfoo'


def test_barcode_data_delayify_long():
    assert barcode.delayify('foo', 2) == '~d~dfoo'


def test_barcode_data_textify():
    assert barcode.textify('foo') == '~dfoo~d~t'


def test_barcode_data_listify():
    assert barcode.listify('foo') == '~d\x20~dfoo~d~e~d~t'


def test_form_instructions_object_instantiates():
    assert instructions

def test_get_instructions_method():
    assert instructions.new_asset('1234567', 'admin', 'Desktop')
