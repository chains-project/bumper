Here's the fixed version of the `getClassesLoc` method using the new library version:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, getTestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}

private static TestListResolver getTestListResolver() {
    CommandLineConfigurationFactory commandLineConfigurationFactory = new CommandLineConfigurationFactory();
    commandLineConfigurationFactory.getClasspathForkConfiguration().getForkOptions().setBootClassPath(getBootClassPath());
    return commandLineConfigurationFactory.createTestListResolver();
}

private static String getBootClassPath() {
    return System.getProperty("sun.boot.class.path");
}
```

The changes include creating a new method `getTestListResolver` to get the `TestListResolver` instance and using the new method `createTestListResolver` from the `CommandLineConfigurationFactory`. Additionally, the `getWildcard` method is called on the returned `TestListResolver` instance.

The `getBootClassPath` method is introduced to get the boot classpath for the `ClasspathForkConfiguration`.

The `DirectoryScanner` constructor now takes a `String` as the second argument instead of the removed `TestListResolver` method `getWildcard()`. This change is required because the new library version removes the `getWildcard()` method from the `TestListResolver` class.

Finally, the `DirectoryScanner` constructor is modified to use the `CommandLineConfigurationFactory` to create the `DirectoryScanner` instance, allowing the use of the new library methods.