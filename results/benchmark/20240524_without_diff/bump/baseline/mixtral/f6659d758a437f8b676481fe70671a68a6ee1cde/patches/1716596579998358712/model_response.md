Here is a possible patch for the failing code:

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

    Yaml yaml = new Yaml(constructor, representer);

    try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
        return yaml.loadAs(reader, clazz);
    } catch (FileNotFoundException e) {
        throw new RuntimeException(e);
    }
}
```

The main change is the use of the `loadAs` method instead of `load` to read the YAML file and deserialize it into an instance of the specified class. This method was added in SnakeYAML version 1.28, so it should be available in recent versions of the library.

Note that the `FileReader` constructor used in the `loadAs` method call is not marked as deprecated or removed in the Java SE API documentation. However, if you prefer to avoid using it, you can replace it with a `InputStreamReader` constructor that takes a `FileInputStream` argument. For example:

```java
Yaml yaml = new Yaml(constructor, representer);

try (FileInputStream inputStream = new FileInputStream(path);
     InputStreamReader reader = new InputStreamReader(inputStream)) {
    return yaml.loadAs(reader, clazz);
} catch (FileNotFoundException e) {
    throw new RuntimeException(e);
}
```

This version of the code uses the `FileInputStream` class to read the contents of the file as a stream of bytes, and then wraps it in an `InputStreamReader` to convert the bytes to characters using the default character encoding of the platform. This approach is more flexible than the `FileReader` constructor, as it allows you to specify a different character encoding if needed. However, it is slightly more verbose and requires the use of two classes instead of one.