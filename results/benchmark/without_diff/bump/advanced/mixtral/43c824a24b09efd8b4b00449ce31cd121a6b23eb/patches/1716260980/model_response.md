Here is a possible patch for the failing client code:
```java
private static java.util.List<java.lang.String> extractList(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, Object branch) {
    java.util.List<de.gwdg.metadataqa.api.model.XmlFieldInstance> instances = cache.get(getStringPath(branch));
    java.util.List<java.lang.String> values = new java.util.ArrayList<>();
    if (instances != null)
        for (de.gwdg.metadataqa.api.model.XmlFieldInstance instance : instances)
            values.add(instance.getValue());

    return values;
}

private static java.lang.String getStringPath(Object branch) {
    // implementation depends on the actual structure of the 'branch' object
    // for example, if 'branch' is a JsonNode, you can use the following code:
    // return branch.get("jsonPath").asText();
    throw new UnsupportedOperationException();
}
```
The patch involves changing the type of the `branch` parameter from `JsonBranch` to `Object`, and using a helper method `getStringPath()` to extract the JSON path from the `branch` object. The implementation of `getStringPath()` depends on the actual structure of the `branch` object, and should be adapted accordingly.

Note that this patch assumes that the `JsonBranch` class has been removed, and that the `JsonPathCache` class now accepts a `String` parameter instead of a `JsonBranch` parameter. If this is not the case, the patch may need to be adjusted accordingly.