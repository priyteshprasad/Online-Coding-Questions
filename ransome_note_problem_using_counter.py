# ransome note question
# Find(T of F), if it is possible to create note using letters of magazine

from collections import Counter

def ransome_note(magazine = [], note = []):
  mag_counter = Counter(magazine)
  note_counter = Counter(note)
  
  
  print(mag_counter)
  print(note_counter)
  # print(mag_counter or note_counter)
  return mag_counter & note_counter == note_counter


magazine = "give me one grand today night".split()
note = "give me grand today".split()
assert ransome_note(magazine, note) is True
print("\n")
magazine = "two times three is not four".split()
note = "two times two is four".split()
assert ransome_note(magazine, note) is False
print("\n")
magazine = "i asked him his name and he did not reply which made me thinks is he a good man we need or is he just a person of different appearance looking like the one we want to give that they he him his".split()
note = "did he give his name".split()
assert ransome_note(magazine, note) is True