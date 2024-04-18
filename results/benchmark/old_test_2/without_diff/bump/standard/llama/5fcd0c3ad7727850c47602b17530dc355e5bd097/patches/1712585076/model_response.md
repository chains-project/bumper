Here's a possible patch to fix the error:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass())));
}
```

The patch replaces the failing method `getClassInfo` with a new method `getClassInfoFromSet` that takes a `java.util.Set` of `org.pitest.classinfo.ClassName` objects instead of a single `org.pitest.classinfo.ClassName` object. The new method uses the `Stream` API to filter the elements of the `Set` and then returns the first element of the resulting stream.

Here's the patch in code:
```diff
-    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass())));
+    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromSet(coverage, data.getMutatedClass()));

+private static org.pitest.classinfo.ClassInfo getClassInfoFromSet(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName clazz) {
+    return coverage.getClassInfo(java.util.stream.Stream.of(clazz).filter(c -> c.getName().equals(clazz.getName())).findFirst().orElseThrow(() -> new RuntimeException("Class not found: " + clazz)));
+}
```
This patch should fix the error by providing a working implementation of the `getClassInfo` method that takes a `java.util.Set` of `org.pitest.classinfo.ClassName` objects.