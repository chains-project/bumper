```java
public <T extends MockBaseEntity> T createMockEntity(Class<T> clazz, String path) {
    final LoaderOptions loadingConfig = new LoaderOptions();

    final Representer representer = new Representer(new DumperOptions());
    final Tag zoneIdTag = new Tag("!ZoneId");
    representer.addClassTag(ZoneId.class, zoneIdTag);
    final Tag localDateTag = new Tag("!LocalDate");
    representer.addClassTag(LocalDate.class, localDateTag);

    final Constructor constructor = new Constructor(clazz, loadingConfig) {{
        this.addTypeDescription(new TypeDescription(ZoneId.class, "ZoneId"));
        this.addTypeDescription(new TypeDescription(LocalDate.class, "LocalDate"));

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
In this updated code, I have removed the line that creates and sets a new instance of TrustedTagInspector. This class has been removed in the new library version, so we can't use it anymore. This change should fix the compilation error you were seeing.