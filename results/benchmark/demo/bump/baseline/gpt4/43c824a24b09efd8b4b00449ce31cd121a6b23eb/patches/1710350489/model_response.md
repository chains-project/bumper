It seems like the issue here is that the JsonBranch class cannot be found. This could be due to a number of reasons, such as the library not being included in the project's dependencies, the library not being imported correctly, or the class being moved or renamed in a library update.

However, since I can only modify the client code and not the project's dependencies, I'll assume that the issue is with the import statement itself.

Here is the corrected code:

```java
  import de.gwdg.metadataqa.api.schema.JsonBranch;
```

In this patch, I've changed the package of the JsonBranch class from `de.gwdg.metadataqa.api.json` to `de.gwdg.metadataqa.api.schema`. This is based on the assumption that the class has been moved or renamed in a recent update of the library. You'll need to make sure that this is the correct package for the JsonBranch class in the version of the library you're using.