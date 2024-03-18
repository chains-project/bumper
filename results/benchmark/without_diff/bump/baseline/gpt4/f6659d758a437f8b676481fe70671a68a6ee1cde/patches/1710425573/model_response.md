```java
public <T extends MockBaseEntity> T createMockEntity(Class<T> clazz, String path) {
    final LoaderOptions loadingConfig = new LoaderOptions();
    loadingConfig.setTagInspector(new TrustedTagInspector());

    final Representer representer = new Representer(new DumperOptions());
    final Tag zoneIdTag = new Tag("!ZoneId");
    representer.addClassTag(ZoneId.class, zoneIdTag);
    final Tag localDateTag = new Tag("!LocalDate");
    representer.addClassTag(LocalDate.class, localDateTag);

    final Constructor constructor = new Constructor(clazz) {{
        this.addTypeDescription(new TypeDescription(ZoneId.class, zoneIdTag));
        this.addTypeDescription(new TypeDescription(LocalDate.class, localDateTag));

        this.yamlConstructors.put(zoneIdTag, new JavaZoneIdConstruct());
        this.yamlConstructors.put(localDateTag, new JavaLocalDateConstruct());
    }};

    Yaml yaml = new Yaml(constructor, representer);

    try {
        return yaml.load(new BufferedReader(new FileReader(path)));
    } catch (FileNotFoundException e) {
        throw new RuntimeException(e);
    }
}
```
The issue seems to be with the `Constructor` class. The `Constructor` class does not have a constructor that takes two arguments. I removed the `loadingConfig` from the `Constructor` instantiation as it seems to be the cause of the error. The `Constructor` class in the YAML library only accepts a `Class` as a parameter in its constructor.