```java
@Override
    public Policy<?> getPolicy(final PolicyConfig config) {
        final PolicyConfig sub = config.config("storage");
        try {
            final Config cfg = new Config.Simple();
            cfg.setString("type", sub.string("type"));
            cfg.set("config", sub.toString());
            return new YamlPolicy(
                new BlockingStorage(
                    new StoragesLoader().newObject(
                        sub.string("type"), cfg
                    )
                )
            );
        } catch (final IOException err) {
            throw new UncheckedIOException(err);
        }
    }
```