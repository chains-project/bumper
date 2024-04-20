Here's a fixed version of the `extractList` method that removes the dependency on `JsonBranch`:

```java
private static java.util.List<java.lang.String> extractList(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, java.lang.String jsonPath) {
    java.util.List<de.gwdg.metadataqa.api.model.XmlFieldInstance> instances = cache.get(jsonPath);
    java.util.List<java.lang.String> values = new java.util.ArrayList<>();
    if (instances != null)
        for (de.gwdg.metadataqa.api.model.XmlFieldInstance instance : instances)
            values.add(instance.getValue());

    return values;
}
```

This version of the method takes a `String` argument `jsonPath` instead of a `JsonBranch` argument. It then passes `jsonPath` directly to the `get` method of `JsonPathCache` instead of calling a method on `JsonBranch` to get the JSON path. This removes the dependency on `JsonBranch` and should fix the compilation error.