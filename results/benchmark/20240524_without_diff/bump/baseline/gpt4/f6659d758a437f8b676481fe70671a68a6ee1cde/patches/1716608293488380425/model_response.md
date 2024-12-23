```java
public <T extends MockBaseEntity> T createMockEntity(Class<T> clazz, String path) {
    final LoaderOptions loadingConfig = new LoaderOptions();
    loadingConfig.setTagInspector(new TrustedTagInspector());

    final Representer representer = new Representer(new DumperOptions());
    final Tag zoneIdTag = new Tag("!ZoneId");
    representer.addClassTag(ZoneId.class, zoneIdTag);
    final Tag localDateTag = new Tag("!LocalDate");
    representer.addClassTag(LocalDate.class, localDateTag);

    final Constructor constructor = new Constructor(clazz);
    {
        constructor.setPropertyUtils(new PropertyUtils(loadingConfig));
        constructor.addTypeDescription(new TypeDescription(ZoneId.class, "ZoneId"));
        constructor.addTypeDescription(new TypeDescription(LocalDate.class, "LocalDate"));

        constructor.getYamlConstructors().put(zoneIdTag, new JavaZoneIdConstruct());
        constructor.getYamlConstructors().put(localDateTag, new JavaLocalDateConstruct());
    };

    Yaml yaml = new Yaml(constructor, representer);

    try {
        return yaml.load(new BufferedReader(new FileReader(path)));
    } catch (FileNotFoundException e) {
        throw new RuntimeException(e);
    }
}
```