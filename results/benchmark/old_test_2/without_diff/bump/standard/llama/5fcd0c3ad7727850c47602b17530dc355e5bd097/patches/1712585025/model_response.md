Here's a possible patch to fix the error:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfo(data.getMutatedClass().getName()));
}
```
The patch replaces the line `coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass()));` with `coverage.getClassInfo(data.getMutatedClass().getName());`.


The `getClassInfo` method takes a `ClassName` parameter, but `java.util.Collections.singleton(data.getMutatedClass())` returns a `Set` of `ClassName` objects. Therefore, the patch removes the unnecessary `java.util.Collections.singleton` call and passes the `ClassName` object directly to `getClassInfo`.