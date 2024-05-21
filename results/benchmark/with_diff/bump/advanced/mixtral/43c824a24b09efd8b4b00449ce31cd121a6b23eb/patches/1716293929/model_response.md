Here is a fixed version of the `extractFirst` method that uses the new location of the `JsonBranch` class:

```java
private static java.lang.String extractFirst(de.gwdg.metadataqa.api.model.pathcache.JsonPathCache cache, de.gwdg.metadataqa.api.json.JsonBranch branch) {
    java.util.List<java.lang.String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, branch);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```

Note that I imported the new `JsonBranch` class at the top of the file like this:

```java
import de.gwdg.metadataqa.api.json.JsonBranch;
```

This should fix the "cannot find symbol" error you were seeing.