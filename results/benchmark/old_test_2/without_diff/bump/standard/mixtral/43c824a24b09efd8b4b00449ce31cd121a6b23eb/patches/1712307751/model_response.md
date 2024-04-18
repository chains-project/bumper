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

In this version, we removed the `branch` parameter from the method signature and replaced it with a `jsonPath` parameter of type `String`. We then use this `jsonPath` string to fetch the instances from the `JsonPathCache`. This way, we avoid using the `JsonBranch` class altogether.