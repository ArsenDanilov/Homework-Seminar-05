def correct_text(text):
    if 'абв' in text:
        newtext = text.replace('абв', '')
    print(newtext)


correct_text('Абворожительный абвивалентный абвросий')
