Based on the given changes in the library, the method `getWildcard()` in `TestListResolver` class has been removed. However, the error message does not provide any information about the replacement for this method. Hence, we cannot directly provide a fix for this error. 

However, as a workaround, you can comment out or remove the line that calls the `getWildcard()` method. This will prevent the error from occurring, but it may affect the functionality of your code if the `getWildcard()` method performs an important task. 

Here is the updated code:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    //DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder);
    return directoryScanner.scan().getClasses();
}
```
This code will compile successfully, but you need to ensure that the removal of `getWildcard()` method does not affect the functionality of your code. 

If `getWildcard()` method is crucial for your code, you need to look for its replacement in the new version of the library or you may need to implement its functionality on your own.