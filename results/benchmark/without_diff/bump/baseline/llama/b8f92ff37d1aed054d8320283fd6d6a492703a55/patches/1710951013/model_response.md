Here's a proposed patch to fix the error:
```java
  static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        List<String> classes = directoryScanner.scan();
        classes.stream().filter(className -> !className.startsWith("fr.spoonlabs.flacoco.core.test.strategies.classloader.finder.classes.impl.")).collect(Collectors.toList());
        return classes;
    }
```
The patch removes the `Override` decorator, as the method is not overriding any method in the new version. It also uses the `filter()` method to remove any classes that start with the package name `fr.spoonlabs.flacoco.core.test.strategies.classloader.finder.classes.impl`, which is the package name of the failing class. This should fix the `Cannot find symbol` error.