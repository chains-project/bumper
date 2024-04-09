Here's a possible patch to fix the error:
```java
import org.codehaus.plexus.util.DirectoryScanner;

// Create a new variable to hold the scanner
DirectoryScanner scanner = new DirectoryScanner();

// Replace the failing line with the new scanner
scanner.scan("myfaces-tobago/tobago-tool/tobago-theme-plugin/src/main/java");
```
This patch creates a new `DirectoryScanner` object and assigns it to a variable called `scanner`. Then, it replaces the failing line with a call to the `scan()` method of the `scanner` object, passing the same argument as before.

Note that this patch assumes that the `DirectoryScanner` class is still available and has a `scan()` method that takes a string argument. If this is not the case, a different patch may be needed.