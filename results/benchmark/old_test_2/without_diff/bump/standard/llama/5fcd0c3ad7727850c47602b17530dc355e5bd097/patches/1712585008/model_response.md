Here's a possible patch to fix the error:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfo(data.getMutatedClass().getName()));
}
```
The patch replaces the line `coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass()));` with `coverage.getClassInfo(data.getMutatedClass().getName());`.


The error was caused by the fact that the `getClassInfo` method expects a `java.util.Set` of `org.pitest.classinfo.ClassName` objects, but the `java.util.Collections.singleton` method returns a `java.util.Set` of a single `org.pitest.mutationtest.ClassMutationResults` object.

The patch fixes the issue by passing the name of the mutated class instead of the `ClassMutationResults` object directly to the `getClassInfo` method.