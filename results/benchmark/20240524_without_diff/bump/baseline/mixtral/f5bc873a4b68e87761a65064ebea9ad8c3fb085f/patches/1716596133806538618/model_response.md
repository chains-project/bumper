Here's a possible patch for the failing client code:

```java
import org.codehaus.plexus.components.io.file.FileScanner;

// ...
DirectoryScanner directoryScanner = new DirectoryScanner();
directoryScanner.setBasedir(basedir);
directoryScanner.setIncludes(new String[]{ "**/*.xhtml" });
directoryScanner.scan();
String[] files = directoryScanner.getIncludedFiles();
// ...
```

This patch replaces the failing import statement with the correct one, and creates a new `DirectoryScanner` instance. The `setBasedir`, `setIncludes`, `scan`, and `getIncludedFiles` methods are used to configure and scan the directory for the desired files.