Here's the proposed patch for the failing client code:

```java
private static java.util.List<java.lang.String> extractList(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.api.json.DataElement element) {
    java.util.List<de.gwdg.metadataqa.api.model.XmlFieldInstance> instances = cache.get(element.getJsonPath());
    java.util.List<java.lang.String> values = new java.util.ArrayList<>();
    if (instances != null)
        for (de.gwdg.metadataqa.api.model.XmlFieldInstance instance : instances)
            values.add(instance.getValue());

    return values;
}
```

The changes include updating the type of the `branch` parameter to `DataElement` from `JsonBranch` in the method signature, and updating the corresponding variable inside the method. This is based on the addition of the `DataElement` class with the same method signatures as `JsonBranch` in the new library version.