Here's the updated `extractFirst` method that uses a `JsonBranchAdapter` to adapt the new library type:

```java
import de.gwdg.metadataqa.marc.JsonBranchAdapter;

private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, Object branch) {
    java.util.List<java.lang.String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, new JsonBranchAdapter(branch));
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```

This solution creates a `JsonBranchAdapter` that adapts the new library type `Object` to the old type `JsonBranch`.