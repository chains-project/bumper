Here's a possible patch to fix the error:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfo(data.getMutatedClass().getName()));
}
```
The patch replaces the line `coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass()));` with `coverage.getClassInfo(data.getMutatedClass().getName());`.


The `getClassInfo` method is not able to accept a `java.util.Set` parameter, so we need to pass the class name as a string instead.

With this patch, the method call `coverage.getClassInfo(data.getMutatedClass().getName())` should resolve the error and allow the code to compile successfully.