import markovify

# Get raw text as string.
with open("/home/unyxt/manifiestas/txt-manifiestas/m-ES-FeministNoDataManifiesto.txt") as f:
    text_a = f.read()
with open("/home/unyxt/manifiestas/txt-manifiestas/m-ES-ManifiestoCiberfeminista.txt") as g:
    text_b = g.read()
with open("/home/unyxt/manifiestas/txt-manifiestas/m-ES-ManifiestoDeLaZorraMutante.txt") as h:
    text_c = h.read()
with open("/home/unyxt/manifiestas/txt-manifiestas/m-ES-ManifiestoPorAlgoritmiasHackfeministas.txt") as j:
    text_d = j.read()



# Build the model.
#text_model = markovify.Text(text)

model_nodata = markovify.Text(text_a)
model_ciberfem = markovify.Text(text_b)
model_mutant = markovify.Text(text_b)
model_hackfem = markovify.Text(text_b)
model_combo = markovify.combine([ model_nodata, model_ciberfem, model_mutant, model_hackfem ], [ 0.2, 1.0, 0.8, 0.4 ])


# Print five randomly-generated sentences
for i in range(20):
    print(model_combo.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
for i in range(3):
    print(model_combo.make_short_sentence(280))
    
    
   
