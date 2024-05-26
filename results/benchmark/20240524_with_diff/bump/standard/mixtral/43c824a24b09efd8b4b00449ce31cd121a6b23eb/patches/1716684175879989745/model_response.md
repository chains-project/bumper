Here is the updated `extractFirst` method with the import statement for the new location of the `JsonBranch` class:

```java
import de.gwdg.metadataqa.api.json.JsonBranch;

private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, JsonBranch branch) {
    java.util.List<java.lang.String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, branch);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```