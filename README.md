# Explore HSK - 词语接龙

## Presentation

The goal is to make vocabulary review easier for Mandarin language learners via grouping according to:
- semantic similarity
- character usage
- character radicals (to do)
- pronunciation (to do)

## To build

### 1. Build the model
```bash
cd backend && make build-model
```

This will create a `model.pkl` file in `backend/data/model.pkl`.
It will download and load a [fasttext](https://fasttext.cc/) language model in memory, so make sure to provision enough RAM is your Docker settings.

### 2. Build the app
```bash
# if on local
docker-compose build

# if on server
make build
```

### 2. Deploy frontend and backend
```bash
docker-compose up
```

## Todo
- [ ] Radical decomposition
- [ ] Search
- [ ] Traditional characters
- [ ] pīnyīn diacritics

## References

- HSK word data - https://github.com/Lemmih/lesschobo/tree/master/data
