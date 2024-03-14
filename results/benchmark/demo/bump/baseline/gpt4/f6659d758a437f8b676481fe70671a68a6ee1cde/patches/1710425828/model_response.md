```java
public <T extends MockBaseEntity> T createMockEntity(Class<T> clazz, String path) {
        final LoaderOptions loadingConfig = new LoaderOptions();
        loadingConfig.setTagInspector(new TrustedTagInspector());

        final Representer representer = new Representer(new DumperOptions());
        final Tag zoneIdTag = new Tag("!ZoneId");
        representer.addClassTag(ZoneId.class, zoneIdTag);
        final Tag localDateTag = new Tag("!LocalDate");
        representer.addClassTag(LocalDate.class, localDateTag);

        final Constructor<T> constructor = new Constructor<T>(clazz, loadingConfig) {{
            this.addTypeDescription(new TypeDescription(ZoneId.class, zoneIdTag));
            this.addTypeDescription(new TypeDescription(LocalDate.class, localDateTag));

            this.yamlConstructors.put(zoneIdTag, new ConstructYamlStr());
            this.yamlConstructors.put(localDateTag, new ConstructYamlStr());
        }};

        Yaml yaml = new Yaml(constructor, representer);

        try {
            return yaml.loadAs(new BufferedReader(new FileReader(path)), clazz);
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
    }
```