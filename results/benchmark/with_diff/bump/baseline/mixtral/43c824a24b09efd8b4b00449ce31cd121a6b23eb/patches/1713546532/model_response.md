Here's a proposed patch for the failing client code:

```java
import de.gwdg.metadataqa.json.JsonBranch;

// ...

// Replace any usage of `de.gwdg.metadataqa.api.json.JsonBranch`
// with `de.gwdg.metadataqa.json.JsonBranch`
```

The patch updates the import statement and any usage of `JsonBranch` from `de.gwdg.metadataqa.api.json` to `de.gwdg.metadataqa.json`. This is based on the assumption that the `JsonBranch` class has been moved from the `de.gwdg.metadataqa.api.json` package to the `de.gwdg.metadataqa.json` package in the new library version.