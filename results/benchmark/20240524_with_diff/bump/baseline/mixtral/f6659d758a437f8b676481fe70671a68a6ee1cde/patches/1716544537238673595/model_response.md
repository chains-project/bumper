Here's the patched version of the `createMockEntity` method that should fix the error:

```java
public <T extends MockBaseEntity> T createMockEntity(Class<T> clazz, String path) {
    final LoaderOptions loadingConfig = new LoaderOptions();
    loadingConfig.setTagInspector(new TrustedTagInspector());

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

    Yaml yaml = new Yaml(constructor, representer) {
        @Override
        protected TrustedTagInspector createTagInspector() {
            return new TrustedTagInspector();
        }
    };

    try {
        return yaml.load(new BufferedReader(new FileReader(path)));
    } catch (FileNotFoundException e) {
        throw new RuntimeException(e);
    }
}
```

The changes made are:

* Override the `createTagInspector()` method to create a new instance of `TrustedTagInspector`.

This should fix the error by providing a new way to create the `TrustedTagInspector` instance, as the default constructor seems to have been removed in the new library version.