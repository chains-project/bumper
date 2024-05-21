Here is a patch that you can apply to the failing method:

```java
private static java.util.List<java.lang.String> extractList(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.api.json.JsonBranch branch) {
    java.util.List<de.gwdg.metadataqa.api.model.XmlFieldInstance> instances = cache.get(branch.getJsonPath());
    java.util.List<java.lang.String> values = new java.util.ArrayList<>();
    if (instances != null)
        for (de.gwdg.metadataqa.api.model.XmlFieldInstance instance : instances)
            values.add(instance.getValue());

    return values;
}
```

The only change that was made is that the type of the `branch` parameter was changed from `JsonBranch` to `de.gwdg.metadataqa.api.json.JsonBranch`. This is because the `JsonBranch` class is no longer available in the new library version, and has been replaced by `de.gwdg.metadataqa.api.json.JsonBranch`.