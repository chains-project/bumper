Here's a possible patch to fix the issue:

```java
public <T extends MockBaseEntity> T createMockEntity(Class<T> clazz, String path) {
    final LoaderOptions loadingConfig = new LoaderOptions();
    loadingConfig.setTagInspector(new TrustedTagInspector());

    final Representer representer = new Representer(new DumperOptions());
    final Tag zoneIdTag = new Tag("!ZoneId");
    representer.addClassTag(ZoneId.class, zoneIdTag);
    final Tag localDateTag = new Tag("!LocalDate");
    representer.addClassTag(LocalDate.class, localDateTag);

    ObjectMapper objectMapper = new ObjectMapper(new YAMLFactory());
    JavaTimeModule javaTimeModule = new JavaTimeModule();
    javaTimeModule.addDeserializer(ZoneId.class, new ZoneIdDeserializer());
    javaTimeModule.addDeserializer(LocalDate.class, new LocalDateDeserializer());
    objectMapper.registerModule(javaTimeModule);

    try {
        return objectMapper.readValue(new File(path), clazz);
    } catch (IOException e) {
        throw new RuntimeException(e);
    }
}

static class ZoneIdDeserializer extends StdDeserializer<ZoneId> {
    protected ZoneIdDeserializer() {
        this(null);
    }

    protected ZoneIdDeserializer(Class<?> vc) {
        super(vc);
    }

    @Override
    public ZoneId deserialize(JsonParser p, DeserializationContext ctxt)
      throws IOException, JsonProcessingException {
        return ZoneId.of(p.getText());
    }
}

static class LocalDateDeserializer extends StdDeserializer<LocalDate> {
    protected LocalDateDeserializer() {
        this(null);
    }

    protected LocalDateDeserializer(Class<?> vc) {
        super(vc);
    }

    @Override
    public LocalDate deserialize(JsonParser p, DeserializationContext ctxt)
      throws IOException, JsonProcessingException {
        return LocalDate.parse(p.getText());
    }
}
```

This patch uses the Jackson library to parse the YAML file and deserialize it into the desired class. It also includes custom deserializers for `ZoneId` and `LocalDate` classes, since those are not supported out of the box.

Note that this patch assumes that the `JavaTimeModule` is included in the project's classpath. If it's not, it can be added using a build tool like Maven or Gradle.

Also note that the patch removes the use of the `Constructor` class, which is not needed to deserialize a YAML file using Jackson. Instead, the `ObjectMapper` class is used to read the file and deserialize it into the desired class.

Finally, the patch removes the use of the `TypeDescription` and `JavaZoneIdConstruct` classes, which are not needed to deserialize a YAML file using Jackson. Instead, custom deserializers are used to handle the `ZoneId` and `LocalDate` classes.