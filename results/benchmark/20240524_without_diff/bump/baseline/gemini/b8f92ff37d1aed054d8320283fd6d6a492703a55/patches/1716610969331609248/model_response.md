```java
  static List<String> getClassesLoc(File testSrcFolder) {
        File[] files = testSrcFolder.listFiles(File::isFile);
        List<String> classes = new ArrayList<>();
        if (files != null) {
            for (File file : files) {
                if (file.getName().endsWith(".java")) {
                    classes.add(file.getAbsolutePath());
                }
            }
        }
        return classes;
    }
```