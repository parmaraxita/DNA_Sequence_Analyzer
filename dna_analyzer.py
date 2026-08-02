dna_input = st.text_input("Enter a DNA sequence:")
dna = dna_input.upper()
# ONLY run calculations if text was entered
if dna:
   length = len(dna)
   a = dna.count('A')
   t = dna.count('T')
   g = dna.count('G')
   c = dna.count('C')
    gc_content = ( (g+c) / length) * 100 if length > 0 else 0
    st.subheader('\n-----DNA Analysis Results -----')
    st.write('Sequence:', dna)
    st.write('Length:',length) 
    st.write('GC Content: {:.2f} %'.format(gc_content))
    col1, col2, col3, col4 = st.columns(4)
    col1.metric('A:',a)
    col2.metric('T:',t)
    col3.metric('G:',g)
    col4.metric('C:',c) 
