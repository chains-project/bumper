It seems like the method `getWildcard()` has been removed from the `TestListResolver` class in the new version of the library. The provided changes in the library do not provide a direct replacement for this method. Therefore, without further information on how to replicate the functionality of `getWildcard()`, it's impossible to provide a working solution. 

However, if the `getWildcard()` method was used to get a wildcard string for scanning directories, you might need to replace it with a hardcoded wildcard string or another method that returns a wildcard string. 

Here is a potential fix assuming that `getWildcard()` was meant to return a wildcard string like `"*"`:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    String wildcard = "*"; // or another method that returns a wildcard string
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, wildcard);
    return directoryScanner.scan().getClasses();
}
```
This code replaces the call to `TestListResolver.getWildcard()` with a hardcoded string `"*"`. If the wildcard string is different or needs to be dynamically generated, you will have to replace `"*"` with the appropriate string or method call.