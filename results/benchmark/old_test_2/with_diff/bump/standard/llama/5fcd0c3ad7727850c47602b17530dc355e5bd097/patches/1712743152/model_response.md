Here's a possible patch to fix the error:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass())));
}
```

We can see that the `getClassInfo` method has been removed from the `org.pitest.coverage.CoverageDatabase` interface, so we need to use the `org.pitest.classinfo.ClassInfoVisitor` class to retrieve the `ClassInfo` object. Here's the modified code that should work with the new library version:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), org.pitest.classinfo.ClassInfoVisitor.getClassInfo(data.getMutatedClass()));
}
```
We've replaced the `coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass()));` line with `org.pitest.classinfo.ClassInfoVisitor.getClassInfo(data.getMutatedClass());`, which uses the `ClassInfoVisitor` class to retrieve the `ClassInfo` object for the mutated class.

Note that we've also removed the `java.util.Collections.singleton(data.getMutatedClass());` argument passed to the `getClassInfo` method, as it is no longer needed.