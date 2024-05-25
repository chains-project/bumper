Here's a possible patch for the code:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    FileVisitOption[] options = new FileVisitOption[]{FileVisitOption.FOLLOW_LINKS};
    List<String> classes = new ArrayList<>();
    try (DirectoryStream<Path> stream = Files.newDirectoryStream(testSrcFolder.toPath(), "**/*.class", options)) {
        for (Path entry : stream) {
            classes.add(entry.toAbsolutePath().toString());
        }
    } catch (IOException e) {
        // Handle exception
    }
    return classes;
}
```

This patch uses the Java NIO library to scan the directory and find all the `.class` files. It avoids using the `DirectoryScanner` class, which might have caused the original error. The `DirectoryStream` class is added in Java 7, so it should be available in most modern Java environments.