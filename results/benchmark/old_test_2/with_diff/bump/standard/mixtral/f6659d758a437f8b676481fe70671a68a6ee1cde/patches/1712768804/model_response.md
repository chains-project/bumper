Here is a possible patch for the failing method:

```java
public <T extends com.premiumminds.billy.core.test.fixtures.MockBaseEntity> T createMockEntity(java.lang.Class<T> clazz, java.lang.String path) {
    final org.yaml.snakeyaml.LoaderOptions loadingConfig = new org.yaml.snakeyaml.LoaderOptions();
    loadingConfig.setTag(new org.yaml.snakeyaml.nodes.Tag("!trusted"));
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
        return yaml.load(new java.io.BufferedReader(new java.io.FileReader(path)));
    } catch (java.io.FileNotFoundException e) {
        throw new java.lang.RuntimeException(e);
    }
}
```

The changes I made are:

* I removed the `loadingConfig.setTagInspector(new com.premiumminds.billy.core.test.TrustedTagInspector());` line, since the `TrustedTagInspector` class is no longer available.
* I replaced it with `loadingConfig.setTag(new org.yaml.snakeyaml.nodes.Tag("!trusted"));`, which has the same effect of allowing global tags.
* I removed the `isGlobalTagAllowed` method from the `Constructor` class, since it is no longer necessary.
* I also removed the import statement for `com.premiumminds.billy.core.test.TrustedTagInspector` at the beginning of the file.

Note that these changes may not be sufficient to make the code work correctly, depending on how the `TrustedTagInspector` class was used in the rest of the code. If the `TrustedTagInspector` class was doing some additional checks or modifications to the tags, those may need to be replicated in the new code.