```java
  static List<String> getClassesLoc(File testSrcFolder) {
        final List<String> classes = new ArrayList<>();
        final File[] files = testSrcFolder.listFiles();
        if (files != null) {
            for (final File file : files) {
                if (file.isFile() && file.getName().endsWith(".java")) {
                    classes.add(file.getAbsolutePath());
                }
            }
        }
        return classes;
    }
```