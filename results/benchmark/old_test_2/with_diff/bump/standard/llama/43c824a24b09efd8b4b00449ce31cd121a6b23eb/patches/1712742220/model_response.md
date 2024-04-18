Here's a possible patch to fix the error:
```java
private static java.util.List<java.lang.String> extractList(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.api.model.JsonBranch branch) {
    java.util.List<de.gwdg.metadataqa.api.model.XmlFieldInstance> instances = cache.get(branch.getJsonPath());
    java.util.List<java.lang.String> values = new java.util.ArrayList<>();
    if (instances != null)
        for (de.gwdg.metadataqa.api.model.XmlFieldInstance instance : instances)
            values.add(instance.getValue());

    return values;
}
```
The changes made were:

* Removed the `JsonBranch` parameter and replaced it with `de.gwdg.metadataqa.api.model.JsonBranch`
* Added a diamond operator `<>` to the `List` constructor to avoid the need for explicit type specification
* Removed the `java.util.List` import statement, as it is not needed

This patch should fix the error by using the updated `JsonBranch` class from the new library version.