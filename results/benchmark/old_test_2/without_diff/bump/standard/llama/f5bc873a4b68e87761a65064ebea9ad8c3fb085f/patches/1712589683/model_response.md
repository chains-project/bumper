Here's a proposed patch to fix the error:
```java
import org.codehaus.plexus.util.DirectoryScanner;

// Create a variable to hold the DirectoryScanner instance
DirectoryScanner directoryScanner = new DirectoryScanner();

// Modify the import statement to use the variable
import org.codehaus.plexus.util.DirectoryScanner;

// Replace the failing line with the variable
directoryScanner.setIncludes("**/*.xhtml");
```
This patch creates a variable `directoryScanner` to hold the `DirectoryScanner` instance, and then modifies the import statement to use the variable. The failing line is then replaced with the variable, which should fix the error.

Note that this patch assumes that the `DirectoryScanner` class is still available and has not been removed or modified in the new version of the library. If the class has been removed or modified, a different approach may be necessary.