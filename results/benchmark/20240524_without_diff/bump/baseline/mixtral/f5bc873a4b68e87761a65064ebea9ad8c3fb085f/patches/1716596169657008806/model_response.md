Here's the proposed patch for the failing client code:

```java
import org.codehaus.plexus.components.io.filemanagers.FilteredFileManager;

// ...

public class AbstractThemeMojo {
  // ...

  @Override
  protected FilteredFileManager getFilteredFileManager() {
    return getProject().get filteredFileManager();
  }

  // ...
}
```

In this patch, I replaced the `DirectoryScanner` import with `FilteredFileManager` as it is a more suitable class for the given method. I also changed the method's return type accordingly.