Here's a fixed version of the `createMockEntity` method that uses the new library version:

```java
public <T extends com.premiumminds.billy.core.test.fixtures.MockBaseEntity> T createMockEntity(java.lang.Class<T> clazz, java.lang.String path) {
    final org.yaml.snakeyaml.LoaderOptions loadingConfig = new org.yaml.snakeyaml.LoaderOptions();
    loadingConfig.setAllowDuplicateKeys(true);
    final org.yaml.snakeyaml.representer.Representer representer = new org.yaml.snakeyaml.representer.Representer(new org.yaml.snakeyaml.DumperOptions());
    final org.yaml.snakeyaml.nodes.Tag zoneIdTag = new org.yaml.snakeyaml.nodes.Tag("!ZoneId");
    representer.addClassTag(java.time.ZoneId.class, zoneIdTag);
    final org.yaml.snakeyaml.nodes.Tag localDateTag = new org.yaml.snakeyaml.nodes.Tag("!LocalDate");
    representer.addClassTag(java.time.LocalDate.class, localDateTag);
    final org.yaml.snakeyaml.constructor.Constructor constructor = new org.yaml.snakeyaml.constructor.Constructor(clazz, loadingConfig) {
        {
            this.addTypeDescription(new org.yaml.snakeyaml.TypeDescription(java.time.ZoneId.class, "ZoneId"));
            this.addTypeDescription(new org.yaml.snakeyaml.TypeDescription(java.time.LocalDate.class, "LocalDate"));
            this.yamlConstructors.put(zoneIdTag, new com.premiumminds.billy.core.test.fixtures.JavaZoneIdConstruct());
            this.yamlConstructors.put(localDateTag, new com.premiumminds.billy.core.test.fixtures.JavaLocalDateConstruct());
        }
    };
    org.yaml.snakeyaml.Yaml yaml = new org.yaml.snakeyaml.Yaml(constructor, representer);
    try {
        return yaml.loadAs(new java.io.BufferedReader(new java.io.FileReader(path)), clazz);
    } catch (java.io.FileNotFoundException e) {
        throw new java.lang.RuntimeException(e);
    }
}
```

The changes I made are:

* Replaced `com.premiumminds.billy.core.test.TrustedTagInspector` with `org.yaml.snakeyaml.LoaderOptions.setAllowDuplicateKeys(true)`
* Replaced `yaml.load` with `yaml.loadAs` to avoid the need for a type description for the root object.

Note that the `TrustedTagInspector` class has been removed in the new library version, and its functionality is no longer needed since the `LoaderOptions.setAllowDuplicateKeys(true)` option has been set.