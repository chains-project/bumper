Sure, I understand the constraints. Here's a possible patch for the failing method:
```java
public <T extends MockBaseEntity> T createMockEntity(Class<T> clazz, String path) {
    final LoaderOptions loadingConfig = new LoaderOptions();
    loadingConfig.setTagInspector(new TrustedTagInspector());

    final Representer representer = new Representer(new DumperOptions());
    final Tag zoneIdTag = new Tag("!ZoneId");
    representer.addClassTag(ZoneId.class, zoneIdTag);
    final Tag localDateTag = new Tag("!LocalDate");
    representer.addClassTag(LocalDate.class, localDateTag);

    JavaType zoneIdType = new JavaType(ZoneId.class, "ZoneId", new ConstructYaml(), TypeDescription.NO_DESC);
    JavaType localDateType = new JavaType(LocalDate.class, "LocalDate", new ConstructYaml(), TypeDescription.NO_DESC);

    Constructor constructor = new Constructor(clazz, loadingConfig) {{
        this.addTypeDescription(zoneIdType);
        this.addTypeDescription(localDateType);

        this.yamlConstructors.put(zoneIdTag, new JavaZoneIdConstruct());
        this.yamlConstructors.put(localDateTag, new JavaLocalDateConstruct());
    }};

    Yaml yaml = new Yaml(constructor, representer);

    try {
        return clazz.cast(yaml.load(new BufferedReader(new FileReader(path))));
    } catch (FileNotFoundException e) {
        throw new RuntimeException(e);
    }
}
```
The main changes are:

* Replacing the deprecated `TypeDescription` class with the `JavaType` class.
* Using the `cast` method of the `Class` class to cast the loaded object to the desired type.
* Adding explicit type information to the `JavaType` objects.
* Removing the unused `overrides` variable.
* Adding type information to the constructor instantiation.

I hope this helps! Let me know if you have any questions.