```java
static List<String> getClassesLoc(File testSrcFolder) {
        File[] files = testSrcFolder.listFiles(f -> f.getName().endsWith(".java"));
        List<String> classes = new ArrayList<>();
        if (files != null) {
            for (File file : files) {
                String path = file.getAbsolutePath();
                classes.add(path.substring(0, path.length() - 5));
            }
        }
        return classes;
    }
```