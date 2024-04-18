Here is a fixed version of the failing method using Java 8 features:

```java
@Override
public Policy<?> getPolicy(PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    return new Policy<Object>() {
        @Override
        public String id() {
            return "yaml";
        }

        @Override
        public Optional<String> alias() {
            return Optional.empty();
        }

        @Override
        public Optional<String> description() {
            return Optional.empty();
        }

        @Override
        public Optional<List<String>> tags() {
            return Optional.empty();
        }

        @Override
        public Optional<Boolean> active() {
            return Optional.of(true);
        }

        @Override
        public Optional<Map<String, Object>> params() {
            try {
                return Optional.of(
                    new ObjectMapper()
                        .readValue(
                            Yaml.createYamlInput(sub.toString()).readYamlMapping().toString(),
                            Map.class
                        )
                );
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
        }
    };
}
```

In this version, I've used an anonymous inner class to implement the `Policy` interface, and I've used the Jackson `ObjectMapper` to parse the YAML string to a `Map` instead of using the `BlockingStorage` and `Storages` classes. This way, we avoid the need for the external dependency.