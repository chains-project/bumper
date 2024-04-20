Here's a fixed version of the code that uses `JsonBranch` from the new library version:
```java
private static java.util.List<java.lang.String> extractList(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.api.model.branch.JsonBranch branch) {
    java.util.List<de.gwdg.metadataqa.api.model.XmlFieldInstance> instances = cache.get(branch.getJsonPath());
    java.util.List<java.lang.String> values = new java.util.ArrayList<>();
    if (instances != null)
        for (de.gwdg.metadataqa.api.model.XmlFieldInstance instance : instances)
            values.add(instance.getValue());

    return values;
}
```
In the new library version, `JsonBranch` has been moved to `de.gwdg.metadataqa.api.model.branch` package. Therefore, we need to update the import statement to reflect this change.

Note that I assumed that the new `JsonBranch` class has the same method `getJsonPath()` as in the previous version. If not, you might need to adjust the code accordingly.