Here is a potential patch for the issue:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```
In this patch, the method `getClassInfo` has been replaced with `getClassInfoFor`, which was added in a later version of the library. This should resolve the "cannot find symbol" error.