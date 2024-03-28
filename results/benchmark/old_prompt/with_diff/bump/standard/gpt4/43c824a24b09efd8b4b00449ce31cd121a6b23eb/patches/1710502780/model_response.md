-- de.gwdg.metadataqa.api.model.JsonBranch
++ de.gwdg.metadataqa.api.model.JsonPathBranch

Based on the error message and the changes in the library, it seems that the class `JsonBranch` has been renamed to `JsonPathBranch`. Here is the corrected code:

```java
private static java.util.List<java.lang.String> extractList(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.api.model.JsonPathBranch branch) {
    java.util.List<de.gwdg.metadataqa.api.model.XmlFieldInstance> instances = cache.get(branch.getJsonPath());
    java.util.List<java.lang.String> values = new java.util.ArrayList<>();
    if (instances != null)
        for (de.gwdg.metadataqa.api.model.XmlFieldInstance instance : instances)
            values.add(instance.getValue());


    return values;
}
```