wget https://ftp.ncbi.nlm.nih.gov/pub/lu/PhenoTagger/models.zip
unzip models.zip
rm models.zip
wget https://ftp.ncbi.nlm.nih.gov/pub/lu/PhenoTagger/mutation_disease.zip
mv -i mutation_disease.zip data/mutation_disease.zip
unzip -d data/ data/mutation_disease.zip
rm data/mutation_disease.zip
unzip -d data/ data/corpus.zip
mkdir -p data/distant_train_data
