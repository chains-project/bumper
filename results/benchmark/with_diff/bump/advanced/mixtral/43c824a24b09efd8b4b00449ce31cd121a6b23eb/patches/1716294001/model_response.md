Here's the fixed version of the failing method using the new library version:

```java
private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.api.json.JsonBranch branch) {
    java.util.List<java.lang.String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, branch);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```

The change made is simply updating the import statement for `JsonBranch` to use the new fully qualified name:

```java
import de.gwdg.metadataqa.api.json.JsonBranch;
```

The rest of the code remains unchanged.