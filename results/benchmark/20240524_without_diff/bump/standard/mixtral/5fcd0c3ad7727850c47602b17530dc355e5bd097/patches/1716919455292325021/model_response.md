Here's a possible patch that you can apply to fix the error:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```
In this patch, I replaced the `getClassInfo` method with the `getClassInfoFor` method, which was likely added in a newer version of the `org.pitest.coverage.CoverageDatabase` class. This should fix the "cannot find symbol" error that you encountered.