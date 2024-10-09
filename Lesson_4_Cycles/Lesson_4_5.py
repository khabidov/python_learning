verbs=['state', 'bake', 'open', 'grill', 'talk', 'fake']
past_tense=[]
for verb in verbs:
    if verb[-1]=='e':
        past_tense.append(verb+'d')
    else:
        past_tense.append(verb+'ed')
print(past_tense)