Here's a possible patch to fix the error:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfo(data.getMutatedClass().getName()));
}
```
The patch replaces the line `coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass()));` with `coverage.getClassInfo(data.getMutatedClass().getName());`.


The error was caused by the fact that the `getClassInfo` method takes a `java.util.Set<org.pitest.classinfo.ClassName>` argument, but the `java.util.Collections.singleton(data.getMutatedClass()` argument is a `java.util.Set<java.lang.String>`.

The patch fixes the issue by passing the class name as a string instead of a set of class names, which is what the `getClassInfo` method expects.