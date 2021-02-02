# 单词 explorer

## Presentation

Chinese word visualization tool: the goal is to make vocabulary review easier for Mandarin language learners via grouping according to:
- semantic similarity
- character usage
- character radicals (to do)
- pronunciation (to do)

## To build

### 1. Build the model
```bash
cd backend && make build-model
```

### 2. Build the app
```bash
docker-compose build
```

### 2. Deploy frontend and backend
```bash
docker-compose up
```

## Todo
- [ ] Custom vocabulary list
- [ ] Radical decomposition
- [ ] Pinyin mapping

## References

- HSK word data - https://github.com/Lemmih/lesschobo/tree/master/data
