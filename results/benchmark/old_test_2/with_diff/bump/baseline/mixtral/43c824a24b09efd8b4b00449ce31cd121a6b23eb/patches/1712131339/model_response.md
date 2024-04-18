Here's a possible patch to fix the error:

```java
import de.gwdg.metadataqa.api.schema.json.JsonBranch;
```

Note that I changed the import statement to use `de.gwdg.metadataqa.api.schema.json.JsonBranch` instead of `de.gwdg.metadataqa.api.json.JsonBranch`. This is because the error message suggests that the `JsonBranch` class can no longer be found in the `de.gwdg.metadataqa.api.json` package, but it can be found in the `de.gwdg.metadataqa.api.schema.json` package instead.

I cannot be sure that this patch will work without knowing more about the codebase and the changes made to the library, but it should at least fix the compilation error you encountered.