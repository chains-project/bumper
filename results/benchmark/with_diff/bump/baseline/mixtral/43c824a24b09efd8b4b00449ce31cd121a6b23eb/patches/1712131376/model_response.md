Here's the proposed patch to fix the error:

```java
import de.gwdg.metadataqa.api.schema.json.JsonBranch;
```

Note that I replaced `de.gwdg.metadataqa.api.json` with `de.gwdg.metadataqa.api.schema.json` to import the `JsonBranch` class. This change is based on the assumption that the `JsonBranch` class was moved to a different package in the new library version.