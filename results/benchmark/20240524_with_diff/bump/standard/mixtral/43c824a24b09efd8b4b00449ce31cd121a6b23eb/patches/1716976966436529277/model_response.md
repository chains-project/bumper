Here's the patched version of the `extractFirst` method that uses the new `DataElement` class instead of the removed `JsonBranch` class:

```java
private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.api.json.DataElement branch) {
    java.util.List<java.lang.String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, branch);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```

Note that the `JsonBranch` class has been replaced with `DataElement` in the method signature and in the call to `extractList` method. This should fix the compilation error and allow the code to run with the new library version.