Here's a potential patch that you can apply to the code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

In this patch, I replaced the `getClassInfo` method with the `getClassInfoFor` method, which was likely added in a newer version of the PITest library. This method takes a single `ClassName` argument instead of a `Set<ClassName>`.