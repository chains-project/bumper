Here's the proposed patch:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

In this patch, I replaced the `getClassInfo` method with `getClassInfoFor`, which is a new method added in the `CoverageDatabase` interface. This should resolve the "cannot find symbol" error.