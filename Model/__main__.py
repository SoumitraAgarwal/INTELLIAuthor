import process
import author
import meta

millis 			= meta.initialize_millis()
trainDirectory 	= meta.initialize_train()
docs 			= meta.initialize_docs()
files 			= [trainDirectory + "Doc" + str(x+1) + ".txt" for x in docs]
train 			= process.process_files(files)
millis			= process.log("Opened files in ", millis, 1)

# Doc cleaning

train 			= process.clean_file(train)

mapFirsts, mapCentres, mapLasts, Firsts, Centres, Lasts = process.create_map(train)

# Map with lag 1 (Hope to create a probabilistic model)

millis			= process.log("Processed document in ", millis, 1)
mapRhymes  		= process.get_rhymes(Lasts)
millis 			= process.log("Created rhyme maps for the document in ", millis, 1)
millis 			= process.log("Now I will start writing!\n", millis, 0)

author.write_poem(Firsts, Centres, Lasts, mapFirsts, mapCentres, mapLasts, mapRhymes, 10, 7)