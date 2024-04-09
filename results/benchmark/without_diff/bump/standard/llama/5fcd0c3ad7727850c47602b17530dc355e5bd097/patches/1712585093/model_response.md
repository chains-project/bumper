Here's a possible patch to fix the error:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfo(data.getMutatedClass().getName()));
}
```
The patch replaces the line `coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass()));` with `coverage.getClassInfo(data.getMutatedClass().getName());`.


The `getClassInfo` method takes a `ClassName` parameter, which is a class that represents a Java class. In the original code, `data.getMutatedClass()` returns a `ClassName` object, but `java.util.Collections.singleton(data.getMutatedClass())` wraps it in a `Set` object, which is not what `getClassInfo` expects.

By removing the unnecessary `java.util.Collections.singleton` call and passing `data.getMutatedClass().getName()` directly to `getClassInfo`, the patch fixes the error and allows the code to compile successfully.