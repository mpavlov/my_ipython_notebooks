import pandas
import ddpy
df = pandas.DataFrame({'tune':[61, 60, 60, None, 61, 60, 60, None, 61, 60, 60, None, 68]})
ddpy.to_midi(df, 'vivaldi.mid')
