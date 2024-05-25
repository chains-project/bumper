Here's a fixed version of the code that removes the use of the deprecated `LoaderOptions` class:

```java
public <T extends MockBaseEntity> T createMockEntity(Class<T> clazz, String path) {
    final Representer representer = new Representer(new DumperOptions());
    final Tag zoneIdTag = new Tag("!ZoneId");
    representer.addClassTag(ZoneId.class, zoneIdTag);
    final Tag localDateTag = new Tag("!LocalDate");
    representer.addClassTag(LocalDate.class, localDateTag);

    final Constructor constructor = new Constructor(clazz) {{
        addTypeDescription(new TypeDescription(ZoneId.class, "ZoneId"));
        addTypeDescription(new TypeDescription(LocalDate.class, "LocalDate"));

        yamlConstructors.put(zoneIdTag, new JavaZoneIdConstruct());
        yamlConstructors.put(localDateTag, new JavaLocalDateConstruct());
    }};

    Yaml yaml = new Yaml(constructor, representer);

    try {
        return yaml.load(new BufferedReader(new FileReader(path)));
    } catch (FileNotFoundException e) {
        throw new RuntimeException(e);
    }
}
```

In this version, I have removed the `LoaderOptions` parameter from the `Constructor` constructor and used the default constructor instead. I have also removed the `setTagInspector` method call since it is no longer needed.

Note that this code assumes that the `JavaZoneIdConstruct` and `JavaLocalDateConstruct` classes are still available. If they are not, you may need to replace them with equivalent constructors.