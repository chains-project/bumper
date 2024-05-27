Here is a fixed version of the `extractList` method that uses the new constructor for `JsonBranch`:

```java
private static java.util.List<java.lang.String> extractList(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, String jsonPath) {
    java.util.List<de.gwdg.metadataqa.api.model.XmlFieldInstance> instances = cache.get(jsonPath);
    java.util.List<java.lang.String> values = new java.util.ArrayList<>();
    if (instances != null)
        for (de.gwdg.metadataqa.api.model.XmlFieldInstance instance : instances)
            values.add(instance.getValue());

    return values;
}
```

In this version, I replaced the `JsonBranch` parameter with a `String` parameter that represents the JSON path. This way, we can use the `get` method of the `JsonPathCache` class to retrieve the instances associated with that path.

Note that this version of the method assumes that the `JsonPathCache` object is correctly initialized and contains the necessary data. If that's not the case, you might need to modify the code that creates and populates the `JsonPathCache` object.