Here is a fixed version of the failing method using Java 8 features:

```java
@Override
public Policy<?> getPolicy(PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    return new Policy<Object>() {
        @Override
        public String type() {
            return sub.string("type");
        }

        @Override
        public BlockingStorage value() throws IOException {
            return new BlockingStorage(
                new Storages().newStorage(
                    type(), Yaml.createYamlInput(sub.toString()).readYamlMapping()
                )
            );
        }
    };
}
```

In this version, I have created an anonymous inner class that implements the `Policy` interface, and moved the logic for creating the `BlockingStorage` object into the `value()` method. This allows us to avoid using the `YamlPolicy` constructor, which was causing the "cannot find symbol" error.

Note that this version assumes that the `Policy` interface has two methods: `type()` and `value()`. If the actual interface has different method names, you will need to adjust the code accordingly.

Also note that this version uses a Java 8 lambda expression to create the `Policy` object. If you are using an earlier version of Java, you will need to use an anonymous inner class instead.