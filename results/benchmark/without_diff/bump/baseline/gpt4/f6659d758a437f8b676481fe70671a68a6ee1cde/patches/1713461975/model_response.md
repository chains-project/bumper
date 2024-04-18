```java
public <T extends MockBaseEntity> T createMockEntity(Class<T> clazz, String path) {
        final LoaderOptions loadingConfig = new LoaderOptions();
        loadingConfig.setTagInspector(new TrustedTagInspector());

        final Representer representer = new Representer(new DumperOptions());
        final Tag zoneIdTag = new Tag("!ZoneId");
        representer.addClassTag(ZoneId.class, zoneIdTag);
        final Tag localDateTag = new Tag("!LocalDate");
        representer.addClassTag(LocalDate.class, localDateTag);

        final YamlConstructor constructor = new YamlConstructor(clazz);
        constructor.setPropertyUtils(new PropertyUtils(loadingConfig));
        constructor.addTypeDescription(new TypeDescription(ZoneId.class, zoneIdTag));
        constructor.addTypeDescription(new TypeDescription(LocalDate.class, localDateTag));

        Yaml yaml = new Yaml(constructor, representer);

        try {
            return yaml.load(new BufferedReader(new FileReader(path)));
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
    }
```