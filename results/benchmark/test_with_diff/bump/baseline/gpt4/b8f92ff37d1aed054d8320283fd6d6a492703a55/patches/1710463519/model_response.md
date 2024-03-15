Based on the error message and the changes in the library, it seems that the method `getWildcard()` from the class `TestListResolver` no longer exists or has been changed in the new library version. Unfortunately, none of the new methods added in the library seems to replace the functionality of `getWildcard()`. Therefore, without more context about what `getWildcard()` does or what it is supposed to return, it is impossible to replace it with an equivalent method from the new library. 

The best approach in this case would be to contact the library developers or check the library documentation for more information about the changes and how to adapt the code to the new version. 

However, assuming the `getWildcard()` method was used to return a wildcard string for the directory scanner, you might replace its functionality by manually providing a wildcard string. Here is an example:

```java
  static List<String> getClassesLoc(File testSrcFolder) {
        String wildcard = "*"; // replace this with the appropriate wildcard string
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, wildcard);
        return directoryScanner.scan().getClasses();
    }
```
Please note that this is just a workaround and might not work as expected if `getWildcard()` was doing something more complex.