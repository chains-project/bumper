Sure, here's a possible patch for the failing code:
```java
public <T extends MockBaseEntity> T createMockEntity(Class<T> clazz, String path) {
    final LoaderOptions loadingConfig = new LoaderOptions();
    loadingConfig.setTagInspector(new TrustedTagInspector());

    final Representer representer = new Representer(new DumperOptions());
    final Tag zoneIdTag = new Tag("!ZoneId");
    representer.addClassTag(ZoneId.class, zoneIdTag);
    final Tag localDateTag = new Tag("!LocalDate");
    representer.addClassTag(LocalDate.class, localDateTag);

    JavaType zoneIdType = new JavaType(ZoneId.class, "ZoneId", new TypeDescription(ZoneId.class));
    JavaType localDateType = new JavaType(LocalDate.class, "LocalDate", new TypeDescription(LocalDate.class));

    final Constructor constructor = new Constructor(clazz, loadingConfig) {{
        addTypeDescription(zoneIdType);
        addTypeDescription(localDateType);

        yamlConstructors.put(zoneIdTag, new JavaZoneIdConstruct());
        yamlConstructors.put(localDateTag, new JavaLocalDateConstruct());
    }};

    Yaml yaml = new Yaml(constructor, representer);

    try {
        return yaml.loadAs(new BufferedReader(new FileReader(path)), clazz);
    } catch (FileNotFoundException e) {
        throw new RuntimeException(e);
    }
}
```
The main changes are:

* We create `JavaType` instances for `ZoneId` and `LocalDate` to replace the deprecated `TypeDescription` class.
* We use the `loadAs` method of the `Yaml` class to deserialize the input file directly into an instance of the requested class `T`. This method was added in the SnakeYAML library and can be used instead of manually constructing and parsing the YAML content.